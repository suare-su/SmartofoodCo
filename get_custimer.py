import requests
import json
import re
import datetime

headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "7ff5cfa5"
}
data = {
    "apiLogin": "ff652be7"
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {}
org_url = 'https://api-ru.iiko.services/api/1/organizations'
ORGANIZATION_IDS = [org['id'] for org in requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)
folder = 'GetNewMenu'
label = ''
get_customer_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/get_customer'
#get_customer_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/customer/info'
data = {
    'organizationId': ORGANIZATION_IDS[0],
    'type': 'phone',
    'phone': '+79999999999',
}
customer = requests.post(url=get_customer_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(customer))