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
    "externalMenuId": 4679,
    "organizationIds": ORGANIZATION_IDS,
    "priceCategoryId": '6dce0b44-17af-4c22-94cf-64ad88429a23',
}
#{'correlationId': 'b87c609f-ab40-48bf-9122-1fddad3b6ee2',
# 'externalMenus': [{'id': '4679', 'name': 'В мире животных'}],
# 'priceCategories':
# [{'id': '00000000-0000-0000-0000-000000000000', 'name': 'Базовая категория'},
# {'id': '6dce0b44-17af-4c22-94cf-64ad88429a23', 'name': 'Ценовая категория 1'}]}
current_menu = requests.post(url=MENU_URL_v2, headers=headers, data=json.dumps(data)).json()
print(json.dumps(current_menu))
file2 = open(r"C:\1\%s\all-menu %s %s.txt" % (folder, label, str(datetime.datetime.now())[:19].replace(':','_')),"w+")
file2.write(json.dumps(current_menu))
file2.close()
