import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-eu.iiko.services/api/1/access_token'
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "8825f00c" # client novgorod
}
data = {
    "apiLogin": "7ff5cfa5" # ru demo stand
}
data = {
    "apiLogin": "fb507f8a-b14" # client
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {}
org_url = 'https://api-ru.iiko.services/api/1/organizations'
ORGANIZATION_IDS = [org['id'] for org in requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)

ORGANIZATION_IDS

terminals_url = 'https://api-ru.iiko.services/api/1/terminal_groups'
data = {
    'organizationIds': ORGANIZATION_IDS,
}

TERMINGAL_GROUPS_IDS_RAW = requests.post(url=terminals_url, headers=headers, data=json.dumps(data)).json()['terminalGroups']
print(TERMINGAL_GROUPS_IDS_RAW)
is_alive_url = 'https://api-ru.iiko.services/api/1/terminal_groups/is_alive'
#'items': [{'id': 'fca3d719-a30a-4db5-9ea7-b938e7f56202',
# 'organizationId': '847b26c8-68c3-461a-8511-99c292b9dc16', 'name': 'Группа Ночная доставка', 'address': ''}]
terminals = []
for org in TERMINGAL_GROUPS_IDS_RAW:
    for term in org['items']:
        terminals.append(term['id'])


data = {
    'organizationIds': ORGANIZATION_IDS, #ночная доставка
    'terminalGroupIds': terminals,
}
ALIVE_TERMINALS = requests.post(url=is_alive_url, headers=headers, data=json.dumps(data)).json()
print(ALIVE_TERMINALS)
#time.sleep(30)
MENU_URL = 'https://api-ru.iiko.services/api/1/nomenclature'
ETALON_ORG = 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b' # кролик
ETALON_ORG = '2be1360a-93d0-4b17-82d4-5193a487bc3f' # барсук
#ETALON_ORG = '2d79da61-5843-4dc1-a13d-9db0704c78c1' # новгород
ETALON_ORG =''



# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
def collect_menu(organizationIds, terminals, isSelectedChanged=False, etalon_Organization=None, revisions = [], CollectEtalonOnly = False): # метод, собирающий меню со всех доступных организаций
 # новый параметр CollectEtalonOnly
# ^^^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#
    # organizationIds - массив ID организаций
    # terminals - список терминалов
    # isSelectedChanged - была ли изменена организация по умолчанию
    # etalon_Organization - организация по умолчанию
    # fake - ненужная штука, которая помогает мне делать стресс-тесты метода, убрать из релиза

    all_menu = []
    new_revisions = []

    if etalon_Organization:

        organizationIds.remove(etalon_Organization)
        organizationIds = [etalon_Organization] + organizationIds


    isRevisionChanged = False

    for current_organization in organizationIds: # идем по каждой организации

        data = {
            'organizationId': current_organization,
        }
        current_menu = requests.post(url=MENU_URL, headers=headers, data=json.dumps(data)).json() # запрашиваем меню
        file2 = open(r"C:\1\%s - %s - %s.txt" % (label, current_organization, str(datetime.datetime.now()).replace(':','_').replace('.','_')), "w+")
        file2.write(json.dumps(current_menu))
        file2.close()
        all_menu.append({'menu':current_menu, 'organizationId': current_organization}) # собираем как хомячки
        current_revision = {'revision': current_menu['revision'], 'organizationId': current_organization} # извлекаем ревизию
        new_revisions.append(current_revision) #добавляем в массив ревизий

        if current_revision not in revisions: #проверяем есть ли такая ревизия в старых ревизиях, если нет, то фиксируем изменения
            isRevisionChanged = True

    if not(isRevisionChanged) and not(isSelectedChanged): # если нет изменений и не поменялась эталонная, то бросаем это гиблое дело и идем пить чай
        return None

    # ну а если уж мы дошли до сюда, то приступаем к действительному серьезному занятию и начинаем объединять в одно целое те меню что насобирали

    new_menu = update_menu(all_menu=all_menu, terminals=terminals, CollectEtalonOnly=CollectEtalonOnly)

    return new_menu, new_revisions

# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
def update_menu(all_menu, terminals, CollectEtalonOnly):
    #новый параметр CollectEtalonOnly
# ^^^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#
    # all_menu, массив менюшек которые мы насобирали
    # terminals, список всех терминалов компании

    collected_menu = {
        "groups": [],
        "productCategories": [],
        "products": [],
        "sizes": [],
    }

    prev_terminals = [] # терминалы, организаций, которые уже прошли сбор меню

    for menu in all_menu: # погнали

        current_organization = menu['organizationId']

# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
        isEtalon = False
        if current_organization == all_menu[0]['organizationId']:
            isEtalon = True

        AddNewItems = True
        if CollectEtalonOnly and not(isEtalon):
            AddNewItems = False
        # расставляем флаги
        # isEtalon - проверяем эталонное ли меню (всегда первое),
        # AddNewItems - надо ли добавлять новые позиции
        # CollectEtalonOnly - какое у нас правило сбора данных

# ^^#^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#


        current_menu = menu['menu']

        current_terminals = [] #список терминалов текущей организации
        another_terminals = [] #список терминалов других организаций
        all_terminals = [] #все терминалы всех организаций

        for org in terminals: #распределяем терминалы по массивам
            for terminal in org['items']:
                all_terminals.append({'terminal_id': terminal['id'], 'organizationId': terminal['organizationId']})
                if terminal['organizationId'] == current_organization:
                    current_terminals.append({'terminal_id': terminal['id'], 'organizationId': terminal['organizationId']})
                else:
                    another_terminals.append({'terminal_id': terminal['id'], 'organizationId': terminal['organizationId']})

# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
        if AddNewItems:
            #проверяем группы, категории, размеры и прочее,
            # только если разрешено добавлять новые итемы,
            # разрешение будет всегда при эталонной организации и при флаге CollectEtalonOnly = False
# ^^#^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#
            for current_group in current_menu['groups']: #обновляем список групп
                filtered_menu = list(filter(
                    lambda group: group['id'] == current_group['id'], collected_menu['groups']))
                # пробуем найти такую группу в исходном меню по id группы и id родительской группы
                if not filtered_menu: #если не нашли, то
                    collected_menu['groups'].append(current_group)
                    # если не нашли, то создаем эту группы
            # то же самое делаем с размерами и категориями
            for current_category in current_menu['productCategories']:
                filtered_menu = list(
                    filter(lambda category: category['id'] == current_category['id'], collected_menu['productCategories']))
                if not filtered_menu:
                    collected_menu['productCategories'].append(current_category)

            for current_size in current_menu['sizes']:
                filtered_menu = list(filter(lambda size: size['id'] == current_size['id'], collected_menu['sizes']))
                if not filtered_menu:
                    collected_menu['sizes'].append(current_size)

            # теперь обновляем всю инфу по продуктам, по той же логике, но чуть больше манипуляций

        for current_product in current_menu['products']:
            #сначала также ищем по ИД блюда и ИД родительской папки наличие блюд в меню
            #т.е. либо блюдо уже есть в меню, либо его еще нет


            # Раньше - фильтровали все продукты, ориентируясь на парент групп и id,
            # сейчас если это модификатор - то смотрим только на id
            if current_product['type'] == 'Modifier':
                filtered_menu = list(
                    filter(lambda product: product['id'] == current_product['id'],
                           collected_menu['products']))
            else:

# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
# если задача добавить новые Итемы - то ищем продукт по parrent group и id,
# если же новые итемы не нужны, для нас важны только цены, не важно в какой он папке, главное найти его в целом
                if AddNewItems:
                    filtered_menu = list(
                        filter(lambda product: product['id'] == current_product['id'] and product['parentGroup'] == current_product['parentGroup'],
                               collected_menu['products']))
                else:
                    filtered_menu = list(
                        filter(lambda product: product['id'] == current_product['id'],
                               collected_menu['products']))
# ^^^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#

            # в первую очередь рассмотрим что происходит если оно есть.
            # то есть оно было найдено в эталонном меню, оно может быть как isIncluded в нем, так и нет
            # плюс там могут быть как и размеры которые включены, так и размеры которые выключены в эталонном, но будут включены потом в других
            # Выбранная организация - основа для эталонной, но как мы обсудили - если что-то выключено в выбранной организации, но включено в следующих
            # то мы включаем это в эталонное меню. Такую же логику я применял и на размеры
            if filtered_menu:
                for filtered_product in filtered_menu:

                    index = collected_menu['products'].index(filtered_product)

                    #если это автоматический выгруженный модификатор, то он в любом случае выгрузился, потому что включен в продажу

                    # определяем, первое ли это вхождение блюда в меню организации, или нет
                    FirstDetect = False
                    if current_organization not in collected_menu['products'][index]['DetectedOn']:
                        collected_menu['products'][index]['DetectedOn'].append(current_organization)
                        FirstDetect = True # отмечаем что это первое вхождение в организацию
                        # этот кусок кода работает только в случае, когда мы проверяем вторую и более организацию, т.к.
                        # блюдо УЖЕ есть в выгрузке, но только ПЕРВЫЙ раз встретилось в организации

                    if current_product['type'] == 'Modifier' and FirstDetect:
                        isInclude = True
                    else:
                        isInclude = False

                    # перед тем как начать бегать по размерам, проверяем условия.
                    # (Если это не модификатор) или (Если это модификатор, который первы раз обнаружен в новой организации)
                    # то идем по шагам (чтобы как минимум узнать цены)
                    # если это не модификатор, или он уже не первый раз, то пропускаем всю эту часть
                    if (current_product['type'] != 'Modifier') or (current_product['type'] == 'Modifier' and FirstDetect):

                        for size in current_product['sizePrices']:
                            #ищем эталонный размер, с которым будем сравнивать. Так как блюдо нашлось после фильтра, эталон уже есть, т.к. это не первый цикл
                            etalon_sizePrice = next((price for price in collected_menu['products'][index]['sizePrices'] if price["sizeId"] == size['sizeId']),
                                 None)

                            # если эталон не isIncluded и при этом новый размер isIncluded, то заменим новым размером эталонный
                            if not(etalon_sizePrice["price"]['isIncludedInMenu']) and size['price']['isIncludedInMenu']:

                                etalon_sizePrice["price"]['currentPrice'] = size['price']['currentPrice']
                                etalon_sizePrice["price"]['isIncludedInMenu'] = size['price']['isIncludedInMenu']

                                # и для всех предыдущих терминалов, которые уже до этого прошли проверку, пометим, что там блюдо отличается от эталона
                                # оно там недоступно, и имеет условно недоступную, нулевую цену
                                for terminal in prev_terminals:
                                    collected_menu['products'][index]['differentPricesOn'].append(
                                        {
                                            'terminal_id': terminal['terminal_id'],
                                            'organization_id': terminal['organizationId'],
                                            'size_id': size['sizeId'],
                                            'price': 0,
                                            'is_included': 0,
                                        }
                                    )
                            else:   # если предыдущее условие не выполнено, то просто сравним цены
                                    # если цены не совпадают ИЛИ доступность не совпадает (а чисто гипотетически, блюдо может быть isIncluded в эталонной,
                                    # с нулевой ценой, а в другой организации noIncluded и то же с нулевой ценой
                                    # бред? да. Но мы готовы и к такому!
                                if etalon_sizePrice['price']['currentPrice'] != size['price']['currentPrice'] or etalon_sizePrice['price']['isIncludedInMenu'] != size['price']['isIncludedInMenu']:

                                    for terminal in current_terminals:
                                            collected_menu['products'][index]['differentPricesOn'].append(
                                                {
                                                    'terminal_id': terminal['terminal_id'],
                                                    'organization_id': current_organization,
                                                    'size_id': size['sizeId'],
                                                    'price': size['price']['currentPrice'],
                                                    'is_included': int(size['price']['isIncludedInMenu']),
                                                }
                                            )

                            if size['price']['isIncludedInMenu']:
                                isInclude = True
                            #если хотя бы в одном месте размер доступен к продаже, то запоминаем это

# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
                    if isInclude and FirstDetect: # если хотя бы один размер доступен к продаже, то убираем блюдо из запрета к продаже (по умолчанию все запрещено)
                        for terminal in current_terminals:
                        # добавляем проверку, что мы нашли это блюдо первый раз т.к. это блюдо уже могли удалить ранее
                        # исключаем ошибку
# ^^^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#
                                collected_menu['products'][index]['prohibitedToSaleOn'].remove(terminal)


                    # обновляем Ручную информацию о модификаторе
                    # здесь у нас существует отдельное правило для модификаторов
                    if current_product['type'] == 'Modifier':
                        # мы проверяем условие:
                        # если Ранее сохраненный модификатор в collected_menu имеет одинаковые parentGroup и groupId
                        # то мы делаем выводм, что он выгружен автоматически
                        if collected_menu['products'][index]['parentGroup'] == collected_menu['products'][index]['groupId']:
                            #далее проверяем, как обстоят дела с этими параметрами у модификатора, который мы только что нашли,
                            # напомню, что мы в том участке кода, где мы встречаем то или иное блюдо повторно
                            if current_product['parentGroup'] != current_product['groupId']:
#                               # если у нового модификатора, parentGroup!=groupId, это вручную добавленный модик
                                # и мы забираем у него все параметры, которые задаются в выгрузке
                                collected_menu['products'][index]['order'] = current_product['order']
                                collected_menu['products'][index]['name'] = current_product['name']
                                collected_menu['products'][index]['parentGroup'] = current_product['parentGroup']
                                collected_menu['products'][index]['description'] = current_product['description']
                                collected_menu['products'][index]['additionalInfo'] = current_product['additionalInfo']
                                collected_menu['products'][index]['seoDescription'] = current_product['seoDescription']
                                collected_menu['products'][index]['seoText'] = current_product['seoText']
                                collected_menu['products'][index]['seoKeywords'] = current_product['seoKeywords']
                                collected_menu['products'][index]['seoTitle'] = current_product['seoTitle']
                        # также, если у текущего продукта есть картинки, то мы их все то же забираем, вычищая уникальные
                        if not(collected_menu['products'][index]['imageLinks']): # если фоток ранее сохранено не было
                            if current_product['imageLinks']: #если сейчас фотки есть
                                last_image = current_product['imageLinks'][-1] # то забираем послеюю фотку из массива фотографий
                                collected_menu['products'][index]['imageLinks'].append(last_image)


            else:
# vvvvvvvvvvvvv Новый/измененный код vvvvvvvvvvvvv#
                if AddNewItems:
                    # проверяем эту часть кода только если разрешено добавлять новые итемы (эталонная организация или коллект всего меню)
# ^^^^^^^^^^^^^ Новый/измененный код ^^^^^^^^^^^^^#
                    #теперь глобально рассмотрим что происходит если блюдо не нашлось.
                    # это либо первый цикл, когда мы смотрим только первую организацию, где ничего не находится,
                    # либо это какая-то последующая организация дала нам блюдо (или размер блюда), которое не встретилось в эталоной
                    #все то же самое но создаем блюдо с нуля, вместо того чтоб добавлять его
                    current_product['differentPricesOn'] = []

                    # здесь мы раньше всем продуктам по умолчанию выдавали isInclude False,
                    # теперь если это модик, выдаем isInclude True
                    if current_product['type'] == 'Modifier':
                        if current_product['imageLinks']:
                            current_product['imageLinks'] = [current_product['imageLinks'][-1]] # забираем последнюю фотку из массива фотографий
                        #если это автоматический выгруженный модификатор, то он в любом случае выгрузился, потому что включен в продажу
                        isInclude = True
                    else:
                        isInclude = False

                    # плюс здесь добавили внутренний параметр, чтоб определять первое это вхождение в организацию, или нет
                    current_product['DetectedOn'] = []
                    current_product['DetectedOn'].append(current_organization)




                    for size in current_product['sizePrices']:

                        if size['price']['isIncludedInMenu']:
                            isInclude = True
                        # если хотя бы один размер доступен к продаже, то помечаем его как доступное на точке

                        # если то блюдо, которое мы только что встретили доступно, то
                        # добавляем его как недоступное на все предыдущие терминалы
                        # если организация первая, то предыдущих терминалов - нет (и ничего страшного)
                        # если блюдо встретилось первый раз в неэталонной организации, то здесь будут все терминалы которые уже были проверены до этого
                        # размечаем их как терминалы на которых блюдо недоступно
                            for terminal in prev_terminals:
                                current_product['differentPricesOn'].append(
                                    {
                                        'terminal_id': terminal['terminal_id'],
                                        'organization_id': current_organization,
                                        'size_id': size['sizeId'],
                                        'price': 0,
                                        'is_included': 0,
                                    }
                                )

                    if isInclude:
                        #здесь в зависимости от доступности блюда в текущей организации, либо запрещаем его везде, либо только на остальных терминалах
                        current_product['prohibitedToSaleOn'] = another_terminals.copy()
                    else:
                        current_product['prohibitedToSaleOn'] = all_terminals.copy()

                    collected_menu['products'].append(current_product) # добавляем свеженькое блюдо к старому меню, чтоб не потерялось

        prev_terminals = prev_terminals + current_terminals # пополняем список предыдущих терминалов, только что проверенными терминалами

    return collected_menu

menu, revisions = collect_menu(organizationIds=ORGANIZATION_IDS, terminals=TERMINGAL_GROUPS_IDS_RAW, etalon_Organization=ETALON_ORG, CollectEtalonOnly=True) # собираем меню,
#print(json.dumps(menu))
file2 = open(r"C:\1\all-menu %s %s.txt" % (label, str(datetime.datetime.now()).replace(':','_').replace('.','_')),"w+")
for product in menu['products']:
    if product['differentPricesOn']:
        for price in product['differentPricesOn']:
            print(price['terminal_id'])
    if product['prohibitedToSaleOn']:
        for price in product['prohibitedToSaleOn']:
            print(price['terminal_id'])
file2.write(json.dumps(menu))
file2.close()


# for rev in menu['revisions']:
#     rev['revision'] = rev['revision'] - 1
# print('второй круг')

#menu = collect_menu(organizationIds=ORGANIZATION_IDS, terminals=TERMINGAL_GROUPS_IDS_RAW, revisions=revisions)

