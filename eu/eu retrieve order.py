import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-eu.iiko.services/api/1/access_token'
data = {
    "apiLogin": "8825f00c" # client novgorod
}
data = {
    "apiLogin": "fa7202f0" # client
}
data = {
    "apiLogin": "a9a4d21e-a51" # тест
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {}
org_url = 'https://api-eu.iiko.services/api/1/organizations'
ORGANIZATION_IDS = [org['id'] for org in requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)

ORGANIZATION_IDS

terminals_url = 'https://api-eu.iiko.services/api/1/terminal_groups'
data = {
    'organizationIds': ORGANIZATION_IDS,
}
TERMINGAL_GROUPS_IDS_RAW = requests.post(url=terminals_url, headers=headers, data=json.dumps(data)).json()['terminalGroups']
print(TERMINGAL_GROUPS_IDS_RAW)
#{'id': '2ffb705b-d3d0-2400-017a-7ae49b7200cf',
# 'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f',
# 'name': 'Группа Милый барсук', 'address': ''}
MENU_URL = 'https://api-eu.iiko.services/api/1/nomenclature'
ETALON_ORG = 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b' # кролик
ETALON_ORG = '2be1360a-93d0-4b17-82d4-5193a487bc3f' # барсук
#ETALON_ORG = '2d79da61-5843-4dc1-a13d-9db0704c78c1' # новгород
ETALON_ORG =''

org_id = ORGANIZATION_IDS[0] # кролик
terminal_id = TERMINGAL_GROUPS_IDS_RAW[0]['items'][0]['id']

retrieve_order_url = 'https://api-eu.iiko.services/api/1/deliveries/by_id'

data = {
"organizationId": org_id,
"orderIds": [
"011d0960-c9c8-4888-8f05-628e8f6ea67c"
],
}

order_response = requests.post(url=retrieve_order_url, headers=headers, data=json.dumps(data)).json()

print('--------------order info--------------')
print(json.dumps(order_response))
print('--------------order info--------------')