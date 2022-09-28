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
url = 'https://api-ru.iiko.services/api/1/order/by_id'
data = {
    'organizationIds': [organizationId],
    'orderIds': ['70a460f2-f779-4681-8680-911dc6e9f2ce'],
   # 'posOrderIds': ['15f5025d-1dbf-431a-9a9e-3867f4cb1bfe'],
    'statuses': ['New'],
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

url = 'https://api-ru.iiko.services/api/1/order/by_table'

tables = ["3be7ca30-51a0-445b-adae-4f7c013c9322",
          "52608190-5517-419e-9c87-af8eb321e671",
          "bac01c5d-56d7-4d8f-afe7-4b18660da2f4",
          "18c09cd2-5881-4194-810a-862a3bf01c61",
          "73af7ca2-f67d-4923-8539-f3da7cb2c1f8",]
data = {
    'organizationIds': [organizationId],
    'tableIds': tables,
    'statuses': ['New', 'Bill'],
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

# url = 'https://api-ru.iiko.services/api/1/order/init_by_table'
# data = {
#     'organizationId': organizationId,
#     'terminalGroupId': terminalGroupId,
#     'tableIds': tables,
# }
# response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
# print('---------response---------------')
# print(url)
# print(json.dumps(response))
# print('---------response---------------')
# correlationId  = response['correlationId']
# time.sleep(13)
# url = 'https://api-ru.iiko.services/api/1/commands/status'
# data = {
#     'organizationId': organizationId,
#     'correlationId': correlationId,
# }
# response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
# print('---------response---------------')
# print(url)
# print(json.dumps(response))
# print('---------response---------------')