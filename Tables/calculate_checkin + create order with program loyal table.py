import requests
import json
import re
import datetime
import time
import uuid
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
    "apiLogin": "f2acd906" # client
}
data = {
    "apiLogin": "0c39be08" # тест
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
ETALON_ORG =''

org_id = TERMINGAL_GROUPS_IDS_RAW[0]['organizationId']
terminal_id = TERMINGAL_GROUPS_IDS_RAW[0]['items'][0]['id']
phone ='+79068755752'
#name = 'Игорь'

# Структура заказа
#"id": "3be7ca30-51a0-445b-adae-4f7c013c9322", "number": 1, "name": "\u0421\u0442\u043e\u043b 1"

data = {
    'organizationId': org_id,
    'terminalGroupId': terminal_id,
    #'externalNumber': '111',
   # 'sourceKey': 'stf',
    'order': {
     #     'phone': phone,
     # #   'tableIds': ['3be7ca30-51a0-445b-adae-4f7c013c9322'],
     #    #'phone': phone,
     #    'status': 'New', #Bill Closed Deleted New
     #    # 'customer': {
     #    #  #   'name': '',
     #    # },
     #    'orderServiceType': "Common",
     #  #  'orderTypeId':'bbbef4dc-5a02-7ea3-81d3-826f4e8bb3e0',
         'phone': phone,
        'customer': {
            'name': 'B',
        },
        'orderTypeId':'bbbef4dc-5a02-7ea3-81d3-826f4e8bb3e0',

        'items': [],
        'guests': {
            'count': 4,
        },
    }
}

items = [
    {
        'productId': 'c68e58ae-0de1-49b8-9058-7de83c9a07bd', # Лимонад Манго-Маракуйя
        'type': 'Product',
        'amount': 2,
        'price': 200,
        # 'modifiers': [
        #     {
        #         'productId': '77d21dd7-f684-47f0-86b3-02fd2f5df8c7', # - бекон
        #         'amount': 1,
        #         'productGroupId': 'a0509895-8b0c-4b3a-9810-5ade7ce8b739',# Папка Для вока
        #     }
        # ]
    }

]


data['order']['items'] = items
# data = \
#     {"organizationId":"2be1360a-93d0-4b17-82d4-5193a487bc3f",
#      "terminalGroupId":"2ffb705b-d3d0-2400-017a-7ae49b7200cf",
#      "order":
#          {
#             "id":"ea85d094-9352-4f8b-af72-afa7f11cfc11",
#           "orderTypeId":"bbbef4dc-5a02-7ea3-81d3-826f4e8bb3e0",
#           "items":[{"productId":"45f3ef02-7dd8-4fca-8a07-830e37b16cbd",
#                     "type":"Product","amount":1,"price":150,"positionId":"7f445b6d-b4e7-4192-b1b7-4bc90b5497ed"},
#                    {"productId":"6f4ebd1f-2e2b-427a-8b45-2d36bd3e267d","type":"Product","amount":1,"price":0,"positionId":"b7cb51ad-4de7-5a95-bffb-936b66ccae4d"}],
#           "payments":[{"paymentTypeId":"09322f46-578a-d210-add7-eec222a08871","sum":150,"paymentTypeKind":"Cash"}],
#           "externalNumber":"STF56",
#          # "guestCount": 3,
#
#           "customer":{"name":"Dmtry"},
#           "phone":"+79220465501"}
#      }
#

data['order']['items'] = items


calculate_checkin_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/calculate'
#order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()
calculate_checkin_response = requests.post(url=calculate_checkin_url, headers=headers, data=json.dumps(data)).json()
print('--------------request data--------------')
print(json.dumps(data))
print('--------------request data--------------')
print('--------------calculate_checkin_response--------------')
print(json.dumps(calculate_checkin_response))
print('--------------calculate_checkin_response--------------')

time.sleep(1)

create_order_url = 'https://api-ru.iiko.services/api/1/order/create'
#calculate_checkin_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/calculate'
order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()
#calculate_checkin_response = requests.post(url=calculate_checkin_url, headers=headers, data=json.dumps(data)).json()
to_print = {}
print('--------------request data--------------')
print(json.dumps(data))
to_print['request'] = data
print('--------------request data--------------')
print('--------------order_response--------------')
print(json.dumps(order_response))
#print(json.dumps(calculate_checkin_response))
print('--------------order_response--------------')
time.sleep(3)
get_order_status_url = 'https://api-ru.iiko.services/api/1/commands/status'
correlation_id = order_response['correlationId']
data = {
    'organizationId': org_id,
    'correlationId': correlation_id,
}
#{'correlationId': '42204351-c34d-4a9c-8509-649571568fed', 'orderInfo': {'id': 'ccfb7845-7dc6-42fe-bb56-6f6169929372', 'externalNumber': None, 'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f', 'timestamp': 1653653756471, 'creationStatus': 'InProgress', 'errorInfo': None, 'order': None}}

status_response = requests.post(url=get_order_status_url, headers=headers, data=json.dumps(data)).json()
print('--------------order status--------------')
print(status_response)
print('--------------order status--------------')
