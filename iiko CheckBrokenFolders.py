# import datetime
# import re

# # user_text = 'rsv 09.11.21'
# # text_array = user_text.split(' ')
# # if len(text_array) > 1:
# #     date_array = text_array[1].split('.')
# #     print(date_array)
# #     day = int(date_array[2])
# #     month = int(date_array[1])
# #     if len(date_array[0]) == 2:
# #         year = 2000 + int(date_array[0])
# #     else:
# #         year = int(date_array[0])
# #     try:
# #         date = datetime.date(year, month, day)
# #     except:
# #         print('error while getting date')
# #     return date
# # return datetime.datetime.today() - datetime.timedelta(days=1)
# text1 ='Возмещение ден.ср-в по Дог.экв. ТЭ/021516935 от 2020-06-29. Оборот: 89761 руб.; Комиссия: 1256.71 руб. за 11.01.22. Без НДС. 001-C-267880.'
# text2 ='Эквайринг, по мерчанту 580000093563 от 12.01.2022 операции 29 на сумму 31,090.00 удержано ком 559.62 Возвр 0.00/0.00'
# text3 ='Зачисление средств по операциям эквайринга. Мерчант №581000087202. Дата реестра 12.01.2022. Комиссия 457.47. Возврат покупки 0.00/0.00.НДС не облагается.Удержание за СО0.00' \
#
#
# retext1 = re.findall(r'(?:Комиссия| удержано ком).? (\d+.\d*)', text1) #вытаскиваем комиссия
# retext2 = re.findall(r'ерчант.? №?(\d+)', text3) #вытаскиваем мерчанта
# print(retext1)
#from smsc_api import *
import requests
TOKEN = requests.get('https://iiko.biz:9900/api/0/auth/access_token?user_id=smartofood_biz&user_secret=smarTofood_p@ss13').json()
#ordID = requests.get('https://iiko.biz:9900/api/0/organization/list?access_token=%s' % TOKEN).json()
orgID = '5f850000-90a3-0025-0bec-08d941dcf040'
nomenclature = requests.get('https://iiko.biz:9900//api/0/nomenclature/%s?access_token=%s' % (orgID, TOKEN)).json() #вся номенклатура
AllGroupsNum = len(nomenclature['groups']) # количество папок в полном меню
groups_with_parents = {}
for group in nomenclature['groups']:
    groups_with_parents[group['id']] = {
        'parentGroup': group['parentGroup'],
        'name': group['name']
    }
groupsTree = {} # то меню которое мы построим
nextParentGroups = [] #
#print(nomenclature)
parrentGroups = [[None],] #это массив массивов родительских групп, первый уровень нам известен, это каталог с parrentGroup = None
i = 0 # счетчик цикла, он же счетчик вложенности
while len(groupsTree) < AllGroupsNum: #начнем повторять цикл, пока он наша иерархия не будет включать в себя все папки
    currentLenTree = len(groupsTree) #фиксируем текущую длину нашего меню
    for group in nomenclature['groups']: #пробегаемся по полному меню выгруженному из айки
        if group['parentGroup'] in parrentGroups[i]: # parrentGroups[i] - это список актуальных родительских групп, если проверяемая группа имеет родительскую, которая туда входит, то добавляем ее в groupsTree
            if group['id'] not in groupsTree:
                groupsTree[group['id']] = {
                    'level': i,
                }
                if group['id'] not in nextParentGroups: #сохраняем id текущей группы в список. В первом цикле мы ищем группы которые лежат в 0 уровне. Они же группы первого уровня.
                                                        #во втором цикле будем искать группы которые лежат в группах первого уровня
                    nextParentGroups.append(group['id'])
            else:
                if groupsTree[group['id']]['level'] != i: #если нашли группу, которая уже есть в списке, проверяем совпадает ли уровень. Если да, то  все ок, а если нет - выдаем ошибку
                    print('аларм, папка уже существует в уровне %s а сейчас мы в уровне %s' % (groupsTree[group['id']]['level'], i))
    newLenTree = len(groupsTree) #проверяем изменилось ли наше меню после проверки очередного уровня
    if newLenTree == currentLenTree: #если не изменилась, то выдаем ошибку, и говорим, что такие-то папки не были найдены, что косвенно означает, что они багованные или лежат в багованной
        print('Не нашли %s папок из %s:' % (AllGroupsNum - currentLenTree, AllGroupsNum ))

        for group in nomenclature['groups']:
            if group['id'] not in groupsTree: #выводим на печать те папки, которых нет в нашем дереве
                current_parrents = [group['id']] # фиксируем ветку groupId чтоб не пойти по второму кругу
                parent = group['parentGroup'] # берем родительскую группу
                line = group['name'] + ' \ ' # начинаем рисовать красивый путь
                while parent not in current_parrents: # пока не пойдем по второму кругу - повторять
                    current_parrents.append(parent) #добавляем родителя в массив
                    line = groups_with_parents[parent]['name'] + ' \ ' + line # прокладываем путь
                    parent = groups_with_parents[parent]['parentGroup'] # изменяем родителя
                print(line)
        break # прерываем while
    parrentGroups.append(nextParentGroups) # если все ок, добавляем в список родительский групп новый массив
    nextParentGroups = [] #чистим временный
    i = i + 1 #увеличиваем вложенность




