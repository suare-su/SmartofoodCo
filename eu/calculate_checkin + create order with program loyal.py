import requests
import json
import re
import datetime
import time
import uuid
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
    "apiLogin": "f2acd906" # client
}
data = {
    "apiLogin": "0c39be08" # тест
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
ETALON_ORG =''

org_id = TERMINGAL_GROUPS_IDS_RAW[0]['organizationId']
terminal_id = TERMINGAL_GROUPS_IDS_RAW[0]['items'][0]['id']
phone ='+79068755752'
#name = 'Игорь'

# Структура заказа
data = {
    'organizationId': org_id,
    'terminalGroupId': terminal_id,
   # 'externalNumber': '111',
    #'coupon': 'TST000139',
   # 'sourceKey': 'stf',
    'order': {
        # 'iikoCard5Info': {
        #     'coupon': 'TST000139',
        # },
        'phone': phone,
        'customer': {
         #   'name': '',
        },
        "payments": [
        ],
        'orderServiceType': "DeliveryByCourier",
        'items': [],
        'deliveryPoint': {
            'address': {
                'street': {

                    'classifierId': '72000001000017200',
                  #  'name': 'Сверд',
                  #   'city': 'Тюмень',
                },
                'house': '22',

            }
        }
    }
}


items = [
    {
        'productId': '05af0fa0-51e8-49ba-a0ee-c6f5cf11673f', #Cheeseburger
        'type': 'Product',
        'amount': 1,
        'price': 150,
        "positionId":"4597e942-714f-4226-840e-3c89e6f85298"
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
#data = {"organizationId":"62cc4155-1614-4491-83f3-2cb1c719d3d4","terminalGroupId":"c90e55a2-f4e4-b572-0178-16fe641800cf","order":{"id":"74252a78-2ef2-497f-8f81-6150f0f9681b","phone":"+79082625071","orderTypeId":"5b1508f9-fe5b-d6af-cb8d-043af587d5c2","customer":{"name":"Александр"},"items":[{"productId":"cea0e20c-7ac1-4b31-8814-e0a54e6f036b","type":"Product","amount":1,"price":339,"positionId":"4597e942-714f-4226-840e-3c89e6f85298"},{"productId":"9e5d8555-a940-427c-9fb0-3e804342e29b","type":"Product","amount":1,"price":309,"positionId":"f8d5e2eb-59de-438d-9185-20c8f2f54f3e"}],"payments":[{"paymentTypeId":"09322f46-578a-d210-add7-eec222a08871","sum":648,"paymentTypeKind":"Cash"}],"externalNumber":"STF709","guests":{"count":1,"splitBetweenPersons":False},"comment":""}}
calculate_checkin_url = 'https://api-eu.iiko.services/api/1/loyalty/iiko/calculate'
#order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()
calculate_checkin_response = requests.post(url=calculate_checkin_url, headers=headers, data=json.dumps(data)).json()
print('--------------request data--------------')
print(json.dumps(data))
print('--------------request data--------------')
print('--------------calculate_checkin_response--------------')
print(json.dumps(calculate_checkin_response))
print('--------------calculate_checkin_response--------------')

time.sleep(2)
data['order']['discountsInfo'] = {
    'discounts': [{
        'programId': calculate_checkin_response["loyaltyProgramResults"][0]['marketingCampaignId'],
        'programName': calculate_checkin_response["loyaltyProgramResults"][0]['name'],
        'discountItems': [
            {
                'positionId': calculate_checkin_response["loyaltyProgramResults"][0]['discounts'][0]['orderItemId'],
                'sum': calculate_checkin_response["loyaltyProgramResults"][0]['discounts'][0]['discountSum'],
                'amount': calculate_checkin_response["loyaltyProgramResults"][0]['discounts'][0]['amount'],
            }
        ],
        'type': 'iikoCard',

    }]
}

data['order']['payments'] = [
            {
                "paymentTypeKind": "Cash",
                "sum": 100,
                "paymentTypeId": "09322f46-578a-d210-add7-eec222a08871",
            },
    {
            'paymentTypeKind': 'IikoCard',
            'sum': 15,
            'paymentTypeId': 'e3ff7b26-487c-4467-8b36-f3f3972b94b8',
            'isProcessedExternally': False,
            'paymentAdditionalData': {
                'credential': '+79068755752',
                'searchScope': 'Phone',
    #            'type': 'SyrveCard',
            }
            #  'isFiscalizedExternally': 0,

        }

]
create_order_url = 'https://api-eu.iiko.services/api/1/deliveries/create'
#calculate_checkin_url = 'https://api-eu.iiko.services/api/1/loyalty/iiko/calculate'
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
