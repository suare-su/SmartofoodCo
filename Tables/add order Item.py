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
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}

organizationId = '2be1360a-93d0-4b17-82d4-5193a487bc3f'
terminalGroupId = '2ffb705b-d3d0-2400-017a-7ae49b7200cf'
phone = "+79068755752"
tableIds = ["3be7ca30-51a0-445b-adae-4f7c013c9322"]
orderId = '23d2af8f-06ae-461d-87f4-f929d9e07abd'
url = 'https://api-ru.iiko.services/api/1/order/add_items'
data = {
    'organizationId': organizationId,
    'orderId': 'edd3d6be-1ee9-4214-8070-b8cd1d25ea2c',
   # 'posOrderIds': ['15f5025d-1dbf-431a-9a9e-3867f4cb1bfe'],
   # 'statuses': ['New'],
}
items = [
    {
        'productId': 'c68e58ae-0de1-49b8-9058-7de83c9a07bd', # Лимонад Манго-Маракуйя
        'type': 'Product',
        'amount': 3,
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
data['items'] = items
response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
print('---------print---------------')
print(url)
print('REQUEST-----')
print(json.dumps(data))
print('REQUEST-----')
print('RESPONSE-----')
print(json.dumps(response))
print('RESPONSE-----')
print('---------print---------------')