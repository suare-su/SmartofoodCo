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
    "apiLogin": "a9a4d21e-a51" # eu
}
data = {
    "apiLogin": "a1297eae-e11" # client
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {'returnAdditionalInfo': True}
org_url = 'https://api-eu.iiko.services/api/1/organizations'
org_expand = requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()
print("ORGANIZATIONS: ", org_expand)
ORGANIZATION_IDS = [org['id'] for org in org_expand['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)

ORGANIZATION_IDS

terminals_url = 'https://api-eu.iiko.services/api/1/terminal_groups'
data = {
    'organizationIds': ORGANIZATION_IDS,
}
TERMINGAL_GROUPS_IDS_RAW = requests.post(url=terminals_url, headers=headers, data=json.dumps(data)).json()['terminalGroups']
print(TERMINGAL_GROUPS_IDS_RAW)
#[{'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f',
# 'items': [{'id': '2ffb705b-d3d0-2400-017a-7ae49b7200cf', 'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f', 'name': 'Группа Милый барсук', 'address': ''}]},
# {'organizationId': 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b',
# 'items': [{'id': '46e412c2-c384-4857-a637-5971d0aa1ecf', 'organizationId': 'e7dc065d-2536-4d94-b2d9-f2c56ab8a02b',
# 'name': 'Группа Борзый кролик', 'address': ''}]}]
