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
    "apiLogin": "7ff5cfa5" # тест
}
data = {
    "apiLogin": "bd81486b" # тест
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
name = 'Игорь'

# Структура заказа
data = {
    'organizationId': org_id,
    'terminalGroupId': terminal_id,
    'externalNumber': '111',
    'sourceKey': 'stf',
    'order': {
        'phone': phone,
        'customer': {
            'name': name,
        },
        'orderServiceType': "DeliveryByCourier",
        'items': [],
        'deliveryPoint': {
            'address': {
                'street': {

                    'classifierId': '7200000100001720023',
                    #'name': 'Сверд',
                    #'city': 'Тюмень',
                },
                'house': '22',

            }
        }
    }
}

items = [
    {
        'productId': '45f3ef02-7dd8-4fca-8a07-830e37b16cbd', # Апельсиновый фреш
        'type': 'Product',
        'amount': 1,
        'price': 100,
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
data = {"organizationId":"b861cbc3-461a-4816-b943-b698067d708a","terminalGroupId":"3ee557b2-f52f-2311-017e-6d8142c500cf","order":{"id":"fad27cd6-6012-46a1-b728-da93b85d8f53","phone":"+79167211360","orderTypeId":"76067ea3-356f-eb93-9d14-1fa00d082c4e","customer":{"name":"Валя"},"items":[{"productId":"ae3fbacc-036b-42d8-b74b-6623c548b171","type":"Product","amount":4,"price":270,"positionId":"9187c520-df6a-4c87-a225-fdb633f2ae8a"},{"productId":"55b3e5cb-339d-4d1e-8eeb-a7c87d86a32b","type":"Product","amount":2,"price":385,"positionId":"82d4d824-3248-4b25-8428-201b44bebcac"},{"productId":"4aee537d-9e9c-4645-89b3-84a4de995902","type":"Product","amount":1,"price":380,"positionId":"a59a7ae5-4876-428d-a2ce-80f6a8c2e945"},{"productId":"fa4118ca-a179-4695-bbb1-a927078fc19c","type":"Product","amount":2,"price":290,"positionId":"24439deb-54ef-4a4a-aa0c-caf51d2fe5b9"},{"productId":"1888222f-40b0-4247-be6b-d16016b99115","type":"Product","amount":2,"price":360,"positionId":"cc902cf5-704e-4516-bb63-628027e5ebe8"},{"productId":"0235db65-c6af-457e-99d6-992ac6611fa2","type":"Product","amount":1,"price":250,"positionId":"ef1f485b-f3f0-4322-b433-f145f759dd95"}],"payments":[{"paymentTypeId":"09322f46-578a-d210-add7-eec222a08871","sum":3780,"paymentTypeKind":"Cash"}],"externalNumber":"STF3251","comment":"Просьба доставить во время,ПОЖАЛУЙСТА","completeBefore":"2022-09-15 19:00:00.000","deliveryPoint":{"address":{"street":{"classifierId":"77000000000745200"},"house":"12","flat":"228","entrance":"4","floor":"10"},"coordinates":{"latitude":55.702556000000001,"longitude":37.917205000000003}}}}
#data = {"organizationId":"62cc4155-1614-4491-83f3-2cb1c719d3d4","terminalGroupId":"c90e55a2-f4e4-b572-0178-16fe641800cf","order":{"id":"74252a78-2ef2-497f-8f81-6150f0f9681b","phone":"+79082625071","orderTypeId":"5b1508f9-fe5b-d6af-cb8d-043af587d5c2","customer":{"name":"Александр"},"items":[{"productId":"cea0e20c-7ac1-4b31-8814-e0a54e6f036b","type":"Product","amount":1,"price":339,"positionId":"4597e942-714f-4226-840e-3c89e6f85298"},{"productId":"9e5d8555-a940-427c-9fb0-3e804342e29b","type":"Product","amount":1,"price":309,"positionId":"f8d5e2eb-59de-438d-9185-20c8f2f54f3e"}],"payments":[{"paymentTypeId":"09322f46-578a-d210-add7-eec222a08871","sum":648,"paymentTypeKind":"Cash"}],"externalNumber":"STF709","guests":{"count":1,"splitBetweenPersons":False},"comment":""}}
calculate_checkin_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/calculate'
#order_response = requests.post(url=create_order_url, headers=headers, data=json.dumps(data)).json()
calculate_checkin_response = requests.post(url=calculate_checkin_url, headers=headers, data=json.dumps(data)).json()
print('--------------request data--------------')
print(json.dumps(data))
print('--------------request data--------------')
print('--------------calculate_checkin_response--------------')
#print(json.dumps(order_response))
print(json.dumps(calculate_checkin_response))
print('--------------calculate_checkin_response--------------')