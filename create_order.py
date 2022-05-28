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
phone ='+79068755752'
name = 'Игорь'

# Структура заказа
data = {
    'organizationId': org_id,
    'terminalGroupId': terminal_id,
    'externalNumber': '111',
    'order': {
        'phone': phone,
        'customer': {
            'name': name,
        },
        'orderServiceType': "DeliveryByClient",
        'items': []
    }
}

items = [
    {
        'productId': '01f363b1-9b7e-43a6-bb39-f61a79dcfb4a', # Вок с курицей
        'type': 'Product',
        'amount': 1,
        'modifiers': [
            {
                'productId': '77d21dd7-f684-47f0-86b3-02fd2f5df8c7', # - бекон
                'amount': 1,
                'productGroupId': 'a0509895-8b0c-4b3a-9810-5ade7ce8b739',# Папка Для вока
            }
        ]
    }

]
# Сложное блюдо, вок с говядиной и модиками
items = [
    {
        'primaryComponent': {
            'productId': '6cbfae25-fb9c-40d2-8c0b-fb71bc8199b2', # Вок с курицей
            'modifiers': [
                {
                    'productId': '8c633bd6-718e-4e06-9398-761a491bacd2', # - укроп
                    'amount': 1,
                    'productGroupId': '40e21410-cbb7-43c7-bb66-2a79c446507e', # Папка Допы для WOK
                },
                {
                    'productId': 'b22c9033-e6aa-4648-b138-0a7f3e1f85b0', # - ?
                    'amount': 1,
                }
            ]
        },
        'type': 'Compound',
        'amount': 1,
        'commonModifiers': [
            {
                'productId': '77d21dd7-f684-47f0-86b3-02fd2f5df8c7', # - бекон
                'amount': 1,
                'productGroupId': 'a0509895-8b0c-4b3a-9810-5ade7ce8b739', # Папка Для вока
            },
            {
                'productId': '84278624-f961-43ec-9634-467df36e227b', # - ?
                'amount': 1,
            }
        ]
    }
]

# Сложное блюдо, вок с говядиной и модиками
items = [
    {
        'primaryComponent': {
            'productId': '1d782faa-05f0-4056-8d5a-5d5aa0ea752c', # пицца гавайская
            'modifiers': [
                {
                    'productId': '5d48a355-086c-4659-afc8-4c596f950f1d', # - ?
                    'amount': 1,
                    'productGroupId': '1661c9f4-166c-4929-afd3-7e39ea203767', # ?
                },
            ]
        },
        'secondaryComponent': {
            'productId': '1d782faa-05f0-4056-8d5a-5d5aa0ea752c', # пицца гавайская
            'modifiers': [
                {
                    'productId': '5d48a355-086c-4659-afc8-4c596f950f1d', # - ?
                    'amount': 1,
                    'productGroupId': '1661c9f4-166c-4929-afd3-7e39ea203767', # ?
                },
            ]
        },
        'type': 'Compound',
        'amount': 1,
        'productSizeId' : '8db0efc0-a9d0-4173-8990-083ba1b9f4b9',
        'commonModifiers': [
            {
                'productId': '806cf0b6-b55e-42d6-bc81-f6221fd05d53', # - ?
                'amount': 1,
                'productGroupId': 'ecbc6585-77e2-4706-b79c-0105f7fa33ca', # ?
            }
        ]
    },
    {
        'primaryComponent': {
            'productId': '1d782faa-05f0-4056-8d5a-5d5aa0ea752c', # пицца гавайская
            'modifiers': [
                {
                    'productId': '5d48a355-086c-4659-afc8-4c596f950f1d', # - ?
                    'amount': 1,
                    'productGroupId': '1661c9f4-166c-4929-afd3-7e39ea203767', # ?
                },
            ]
        },
        'type': 'Compound',
        'amount': 1,
        'productSizeId' : '8db0efc0-a9d0-4173-8990-083ba1b9f4b9',
        'commonModifiers': [
            {
                'productId': '806cf0b6-b55e-42d6-bc81-f6221fd05d53', # - ?
                'amount': 1,
                'productGroupId': 'ecbc6585-77e2-4706-b79c-0105f7fa33ca', # ?
            }
        ]
    },
    {
        'primaryComponent': {
            'productId': '6cbfae25-fb9c-40d2-8c0b-fb71bc8199b2', # Вок с курицей
            'modifiers': [
                {
                    'productId': '8c633bd6-718e-4e06-9398-761a491bacd2', # - укроп
                    'amount': 1,
                    'productGroupId': '40e21410-cbb7-43c7-bb66-2a79c446507e', # Папка Допы для WOK
                },
                {
                    'productId': 'b22c9033-e6aa-4648-b138-0a7f3e1f85b0', # - ?
                    'amount': 1,
                }
            ]
        },
        'type': 'Compound',
        'amount': 1,
        'commonModifiers': [
            {
                'productId': '77d21dd7-f684-47f0-86b3-02fd2f5df8c7', # - бекон
                'amount': 1,
                'productGroupId': 'a0509895-8b0c-4b3a-9810-5ade7ce8b739', # Папка Для вока
            },
            {
                'productId': '84278624-f961-43ec-9634-467df36e227b', # - ?
                'amount': 1,
            }
        ]
    }
]


data['order']['items'] = items

create_order_url = 'https://api-ru.iiko.services/api/1/deliveries/create'

order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()

print('--------------request data--------------')
print(json.dumps(data))
print('--------------request data--------------')
print('--------------order response--------------')
print(json.dumps(order_response))
print('--------------order response--------------')
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