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
orderId = 'c4e6a8a3-234e-4778-950f-c9a9993d2386'
url = 'https://api-ru.iiko.services/api/1/order/by_id'
data = {
    'organizationIds': [organizationId],
    'orderIds': ['c4e6a8a3-234e-4778-950f-c9a9993d2386'],
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
