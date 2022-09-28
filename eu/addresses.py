import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-eu.iiko.services/api/1/access_token'
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

regions_url = 'https://api-eu.iiko.services/api/1/regions'
cities_url = 'https://api-eu.iiko.services/api/1/cities'
streets_url = 'https://api-eu.iiko.services/api/1/streets/by_city'
data = {
    'organizationIds': ORGANIZATION_IDS,
}
regions = requests.post(url=regions_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(regions))
#{"correlationId": "0cdf89e5-6cda-4c30-ad65-cefb5962c231", "regions": []}

cities = requests.post(url=cities_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(cities))
#{"correlationId": "1a57a816-1a47-430b-8d6f-06939c950bd6", "cities": [{"organizationId": "b9eede12-44d1-4eaf-9724-1fa9237be4da", "items": [{"id": "b090de0b-8550-6e17-70b2-bbba152bcbd3", "name": "Moscow", "externalRevision": 0, "isDeleted": false, "classifierId": null, "additionalInfo": null}, {"id": "b43fd8e3-1e1c-41b4-bbce-dd3978991e56", "name": "Dubai", "externalRevision": 698, "isDeleted": false, "classifierId": null, "additionalInfo": null}]}]}

data = {
    'organizationId': org_id,
    'cityId': 'a167ab89-1876-ebb4-0182-4d81b702d5bc',
}
streets = requests.post(url=streets_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(streets))