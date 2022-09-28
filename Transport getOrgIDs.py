import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "7ff5cfa5" # тест
}
data = {
    "apiLogin": "e0aa6365" # тест
}

token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {
    'returnAdditionalInfo': True,
    'includeDisabled': True,
}
org_url = 'https://api-ru.iiko.services/api/1/organizations'
response = requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()


print(json.dumps(response))
