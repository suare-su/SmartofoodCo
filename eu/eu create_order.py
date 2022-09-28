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
phone ='+79068755752'
name = 'Игорь'

# Структура заказа
data = {
    'organizationId': org_id,
    'terminalGroupId': terminal_id,
    'order': {
        'phone': phone,
        'customer': {
            'name': name,
        },
       # 'orderServiceType': "DeliveryByClient",
        'orderServiceType': "DeliveryByCourier",

        "deliveryPoint": {
            "coordinates": {
                "latitude": 25.15332,
                "longitude": 55.22523,
             #   "latitude": 25.15332,
            },
            "address": {
                "street": {
                    # "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
                    "name": "hello world",
                    "city": "Dubai"
                },
           # "index": "string",
            "house": "Any random string 22",
            # "building": "string",
            # "flat": "string",
            # "entrance": "string",
            # "floor": "string",
            # "doorphone": "string",
            # "region": {
            # "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            # "name": "string"
            }
        },
        # "externalCartographyId": "string",
        # "comment": "string"
        'items': [],
        },
    }

items = [
    {
        'productId': '05af0fa0-51e8-49ba-a0ee-c6f5cf11673f', #Cheeseburger
        'type': 'Product',
        'amount': 1,
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

create_order_url = 'https://api-eu.iiko.services/api/1/deliveries/create'
#calculate_checkin_url = 'https://api-eu.iiko.services/api/1/loyalty/iiko/calculate'
order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()
#calculate_checkin_response = requests.post(url=calculate_checkin_url, headers=headers, data=json.dumps(data)).json()
print('--------------request data--------------')
print(json.dumps(data))
print('--------------request data--------------')
print('--------------order_response--------------')
print(json.dumps(order_response))
#print(json.dumps(calculate_checkin_response))
print('--------------order_response--------------')
time.sleep(3)
get_order_status_url = 'https://api-eu.iiko.services/api/1/commands/status'
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