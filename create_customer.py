import requests
import json
import re
import datetime

headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "7ff5cfa5"
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
create_customer_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/customer/create_or_update'

data = {
    'organizationId': ORGANIZATION_IDS[0],
    'phone': '+79999999994',
    'name': 'ok2',
    #'consentStatus': 1,
    #'consentSStatus': '+79999999994',
}

customer = requests.post(url=create_customer_url, headers=headers, data=json.dumps(data)).json()
print(customer)