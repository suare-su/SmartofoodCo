import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "8825f00c" # client novgorod
}
data = {
    "apiLogin": "fa7202f0" # client
}
data = {
    "apiLogin": "7ff5cfa5" # тест
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
#{'id': '2ffb705b-d3d0-2400-017a-7ae49b7200cf',
# 'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f',
# 'name': 'Группа Милый барсук', 'address': ''}
MENU_URL = 'https://api-ru.iiko.services/api/1/nomenclature'
ETALON_ORG = 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b' # кролик
ETALON_ORG = '2be1360a-93d0-4b17-82d4-5193a487bc3f' # барсук
#ETALON_ORG = '2d79da61-5843-4dc1-a13d-9db0704c78c1' # новгород
ETALON_ORG =''

org_id = '2be1360a-93d0-4b17-82d4-5193a487bc3f'
terminal_id = '2ffb705b-d3d0-2400-017a-7ae49b7200cf'

retrieve_order_url = 'https://api-ru.iiko.services/api/1/deliveries/by_id'

data = {
"organizationId": org_id,
"orderIds": [
"2953c686-3cc2-4297-a3c5-30c9c7221ac7"
],
}
data = {"organizationId": "e7dc065d-2536-4d94-b2d9-f2c56ab8a02b", "orderIds": ["9adfbd04-03af-9577-0183-2ac27b4d78b6"]}
data = {"organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "orderIds": ["39077032-1596-49a6-b88c-c0644fd842cb"]}
order_response = requests.post(url=retrieve_order_url, headers=headers, data=json.dumps(data)).json()
print('--------------data request--------------')
print(json.dumps(data))
print('--------------data request--------------')

print('--------------order info--------------')
print(json.dumps(order_response))
print('--------------order info--------------')