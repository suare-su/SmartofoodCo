import requests
import json
import re
import datetime

headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "7ff5cfa5"
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {}
org_url = 'https://api-ru.iiko.services/api/1/organizations'
ORGANIZATION_IDS = [org['id'] for org in requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)
folder = 'GetNewMenu'
label = ''
ORGANIZATION_IDS

terminals_url = 'https://api-ru.iiko.services/api/1/terminal_groups'
data = {
    'organizationIds': ORGANIZATION_IDS,
}
TERMINGAL_GROUPS_IDS_RAW = requests.post(url=terminals_url, headers=headers, data=json.dumps(data)).json()['terminalGroups']
print(TERMINGAL_GROUPS_IDS_RAW)
MENU_URL = 'https://api-ru.iiko.services/api/1/nomenclature'
MENUS_URL_v2 = 'https://api-ru.iiko.services/api/2/menu'
MENU_URL_v2 = 'https://api-ru.iiko.services/api/2/menu/by_id'
ETALON_ORG = 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b' # кролик
ETALON_ORG = '2be1360a-93d0-4b17-82d4-5193a487bc3f' # барсук

data = {
}
current_menu = requests.post(url=MENUS_URL_v2, headers=headers, data=json.dumps(data)).json()
print(current_menu)
#{'correlationId': 'e0850348-e8a6-4a1e-ad5b-bc0ac298c305', 'externalMenus': [{'id': '3435', 'name': 'Меню Кролика'}], 'priceCategories': None}
data = {
    "externalMenuId": 5059,
    "organizationIds": ORGANIZATION_IDS,
    "priceCategoryId": '00000000-0000-0000-0000-000000000000',
}
#{'correlationId': 'b87c609f-ab40-48bf-9122-1fddad3b6ee2',
# 'externalMenus': [{'id': '4679', 'name': 'В мире животных'}],
# 'priceCategories':
# [{'id': '00000000-0000-0000-0000-000000000000', 'name': 'Базовая категория'},
# {'id': '6dce0b44-17af-4c22-94cf-64ad88429a23', 'name': 'Ценовая категория 1'}]}
current_menu = requests.post(url=MENU_URL_v2, headers=headers, data=json.dumps(data)).json()
#print(json.dumps(current_menu))
file2 = open(r"C:\1\%s\all-menu %s %s.txt" % (folder, label, str(datetime.datetime.now())[:19].replace(':','_')),"w+")
file2.write(json.dumps(current_menu))
file2.close()
new_menu = {
    'groups': [],
    'productCategories': [],
    'products': [],
    'sizes': [],

}
i = 0
for group in current_menu['itemCategories']:

    print(group['id'])

    if group['buttonImageUrl']:
        imageLinks = [group['buttonImageUrl']]
    else:
        imageLinks = {}

    if group['description']:
        description = [group['description']]
    else:
        description = ""

    new_group = {
        "imageLinks":imageLinks,
        "parentGroup":None,
        "order":i,
        "isIncludedInMenu":True,
        "isGroupModifier":False,
        "id":group['id'],
        "code":"",
        "name":group['name'],
        "description":description,
        "additionalInfo":None,
        "tags":{
        },
        "isDeleted":None,
        "seoDescription":None,
        "seoText":None,
        "seoKeywords":None,
        "seoTitle":None
    }

    new_menu['groups'].append(new_group)

    for item in group['items']:

        new_product = {
            "fatAmount":7,
            "proteinsAmount":6,
            "carbohydratesAmount":18,
            "energyAmount":159,
            "fatFullAmount":21,
            "proteinsFullAmount":18,
            "carbohydratesFullAmount":54,
            "energyFullAmount":477,
            "weight":0.3,
            "groupId":"7a4181d3-5c6d-4a38-9cf6-49ed2f1660b4",
            "productCategoryId":None,
            "type":"Dish",
            "orderItemType":"Compound",
            "modifierSchemaId":"00a7cb5b-21ca-48be-9a19-837793c3bedf",
            "modifierSchemaName":"Вок схема (дополнительно)",
            "splittable":False,
            "measureUnit":"порц",
            "sizePrices":[],
            "modifiers":[],
            "groupModifiers":[],
            "imageLinks":{},
            "doNotPrintInCheque":False,
            "parentGroup":"f08451c9-1900-4aa2-a345-09b89cf235f2",
            "order":0,
            "fullNameEnglish":"",
            "useBalanceForSell":False,
            "canSetOpenPrice":False,
            "id":"6cbfae25-fb9c-40d2-8c0b-fb71bc8199b2",
            "code":"00060",
            "name":"Вок с говядиной",
            "description":"Говядина, овощной микс, лапша удон, кунжут, чесночный соус",
            "additionalInfo":None,
            "tags":{},
            "isDeleted":False,
            "seoDescription":None,
            "seoText":None,
            "seoKeywords":None,
            "seoTitle":None
        }


    i = i + 1


print(json.dumps(new_menu))