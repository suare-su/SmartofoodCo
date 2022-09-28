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

correlationId  = '771fab5b-ff86-473d-a98f-5c1468d657d1'
url = 'https://api-ru.iiko.services/api/1/commands/status'
data = {
    'organizationId': organizationId,
    'correlationId': correlationId,
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