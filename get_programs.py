import requests
import json
import re
import datetime

headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-ru.iiko.services/api/1/access_token'
data = {
    "apiLogin": "3547966a-8bf"
}
data = {
    "apiLogin": "7ff5cfa5"
}
data = {
    "apiLogin": "c6aa4bc0"
}
data = {
    "apiLogin": "3547966a-8bf"
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
get_programs_url = 'https://api-ru.iiko.services/api/1/loyalty/iiko/program'
data = {
    'organizationId': ORGANIZATION_IDS[0],
}
programs = requests.post(url=get_programs_url, headers=headers, data=json.dumps(data)).json()
print(json.dumps(programs))