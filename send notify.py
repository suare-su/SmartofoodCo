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

send_notify_url = 'https://api-ru.iiko.services/api/1/notifications/send'
data = {
    'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f',
    'orderId': 'dcbac48e-f40b-435a-9751-5d1d9beb4620',
    'additionalInfo': 'Строка',
    'orderSource': '',
    'messageType': 'delivery_attention',
}
notify = requests.post(url=send_notify_url, headers=headers, data=json.dumps(data)).json()
print(notify)

data = {
    'organizationId': '2be1360a-93d0-4b17-82d4-5193a487bc3f',
    'correlationId': notify['correlationId'],
}
get_order_status_url = 'https://api-ru.iiko.services/api/1/commands/status'
time.sleep(1)
status_response = requests.post(url=get_order_status_url, headers=headers, data=json.dumps(data)).json()
print('--------------order status--------------')
print(status_response)
print('--------------order status--------------')