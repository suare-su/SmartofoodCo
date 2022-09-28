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
tables = ["3be7ca30-51a0-445b-adae-4f7c013c9322",
          "52608190-5517-419e-9c87-af8eb321e671",
          "bac01c5d-56d7-4d8f-afe7-4b18660da2f4",
          "18c09cd2-5881-4194-810a-862a3bf01c61",
          "73af7ca2-f67d-4923-8539-f3da7cb2c1f8",]

url = 'https://api-ru.iiko.services/api/1/order/close'
data = {
    'organizationId': organizationId,
    'orderId': 'edd3d6be-1ee9-4214-8070-b8cd1d25ea2c',
}

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