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

#[{'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da',
# 'items': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da',
# 'name': 'Group Cute Badger', 'address': ''}]}]
paytypes_url = 'https://api-eu.iiko.services/api/1/payment_types'

PAYTYPES = requests.post(url=paytypes_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(PAYTYPES))
#{'correlationId': '26d53b11-bc4b-4b08-9f87-1574e25f2a59',
# 'paymentTypes': [
# {'id': '09322f46-578a-d210-add7-eec222a08871', 'code': 'CASH', 'name': 'Наличные', 'comment': '', 'combinable': True, 'externalRevision': 1495,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': True, 'paymentProcessingType': 'Both', 'paymentTypeKind': 'Cash', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]},
# {'id': '2119bac0-c1ee-4e69-a12d-5bef755e474a', 'code': 'TIPS', 'name': 'Чаевые на сайте', 'comment': '', 'combinable': True, 'externalRevision': 2271,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': True, 'paymentProcessingType': 'Both', 'paymentTypeKind': 'Card', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]},
# {'id': '559c7a94-8240-4835-a352-7af0a9bb5474', 'code': 'SITE', 'name': 'Онлайн оплата', 'comment': '', 'combinable': True, 'externalRevision': 1495,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': True, 'paymentProcessingType': 'External', 'paymentTypeKind': 'Card', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]},
# {'id': '9921ba7d-088e-4ae1-85ff-d8697b8f869a', 'code': 'TCASH', 'name': 'Чаевые наличные', 'comment': '', 'combinable': True, 'externalRevision': 2295,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': False, 'paymentProcessingType': 'Both', 'paymentTypeKind': 'Cash', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]},
# {'id': 'e7c42b05-3d1e-4c38-a345-ef05e5500ae8', 'code': 'CARD', 'name': 'Банковские карты', 'comment': '', 'combinable': True, 'externalRevision': 1495,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': True, 'paymentProcessingType': 'Both', 'paymentTypeKind': 'Card', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]},
# {'id': 'f9053900-5c5d-4963-a2d5-c45fe56a0baa', 'code': 'TBANK', 'name': 'Чаевые по карте', 'comment': '', 'combinable': True, 'externalRevision': 2295,
#   'applicableMarketingCampaigns': [], 'isDeleted': False, 'printCheque': True, 'paymentProcessingType': 'Both', 'paymentTypeKind': 'Card', 'terminalGroups': [{'id': '48fd91da-ec50-41ab-8a1c-aedcfd96da27', 'organizationId': 'b9eede12-44d1-4eaf-9724-1fa9237be4da', 'name': 'Group Cute Badger', 'address': ''}]}]}

get_tip_url = 'https://api-eu.iiko.services/api/1/tips_types'
TIPS = requests.post(url=get_tip_url, headers=headers).json()
#{'correlationId': '16daa1c9-0a43-45d5-a766-77c22f3bc2b7', 'tipsTypes': [{'id': '0ef8fb9a-57aa-f746-0181-908bfcb8529b', 'name': 'Чаевые', 'organizationIds': ['b9eede12-44d1-4eaf-9724-1fa9237be4da'], 'orderServiceTypes': ['DeliveryPickUp', 'Common', 'DeliveryByCourier'], 'paymentTypesIds': ['09322f46-578a-d210-add7-eec222a08871', '559c7a94-8240-4835-a352-7af0a9bb5474', 'e7c42b05-3d1e-4c38-a345-ef05e5500ae8']}]}

print(TIPS)
# {'correlationId': 'df9fb5cd-d0be-4a4c-9820-6da449ff815e',
# 'tipsTypes': [
# {'id': '0ef8fb9a-57aa-f746-0181-908bfcb87a7b', 'name': 'Еще чаевые (например курьерам)', 'organizationIds': ['b9eede12-44d1-4eaf-9724-1fa9237be4da'],
# 'orderServiceTypes': ['DeliveryByCourier'],
# 'paymentTypesIds': ['9921ba7d-088e-4ae1-85ff-d8697b8f869a']},
# {'id': '0ef8fb9a-57aa-f746-0181-908bfcb8529b', 'name': 'Чаевые +', 'organizationIds': ['b9eede12-44d1-4eaf-9724-1fa9237be4da'],
# 'orderServiceTypes': ['DeliveryPickUp', 'Common', 'DeliveryByCourier'],
# 'paymentTypesIds': ['9921ba7d-088e-4ae1-85ff-d8697b8f869a', 'f9053900-5c5d-4963-a2d5-c45fe56a0baa', '2119bac0-c1ee-4e69-a12d-5bef755e474a']}]}