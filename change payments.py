#{"correlationId": "cbbb9711-e93f-40d9-855a-37eccbb5ca1e",
# "orderInfo": {"id": "99fed126-196b-4595-8b55-470b0cbabf55",
# "externalNumber": null,
# "organizationId": "b9eede12-44d1-4eaf-9724-1fa9237be4da",
# "timestamp": 1656156346311, "creationStatus": "InProgress", "errorInfo": null, "order": null}}
#{"organizationId": "b9eede12-44d1-4eaf-9724-1fa9237be4da",
# "terminalGroupId": "48fd91da-ec50-41ab-8a1c-aedcfd96da27",
# "externalNumber": "111",
# "order": {
# "phone": "+79068755752",
# "customer": {"name": "\u0418\u0433\u043e\u0440\u044c"},
# "orderServiceType": "DeliveryByClient",
# "items": [{"productId": "7ec23c6c-0bef-4cdb-afb6-902ff964cd75", "type": "Product", "amount": 1}],
# "tips": [{"paymentTypeKind": "Cash", "tipsTypeId": "0ef8fb9a-57aa-f746-0181-908bfcb8529b", "sum": 13, "paymentTypeId": "09322f46-578a-d210-add7-eec222a08871"}]}}

import requests
import json
import re
import datetime
import time
label = ''
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
authorization_url = 'https://api-eu.iiko.services/api/1/access_token'
data = {
    "apiLogin": "8825f00c" # client novgorod
}
data = {
    "apiLogin": "fa7202f0" # client
}
data = {
    "apiLogin": "a9a4d21e-a51" # тест
}
token = requests.post(url=authorization_url, headers=headers, data=json.dumps(data)).json()['token']
print("TOKEN: ",token)

headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Authorization':'Bearer %s' % token}
data = {}
org_url = 'https://api-eu.iiko.services/api/1/organizations'
ORGANIZATION_IDS = [org['id'] for org in requests.post(url=org_url, headers=headers, data=json.dumps(data)).json()['organizations']]
print("ORGANIZATIONS: ", ORGANIZATION_IDS)

ORGANIZATION_IDS

terminals_url = 'https://api-eu.iiko.services/api/1/terminal_groups'
data = {
    'organizationIds': ORGANIZATION_IDS,
}
TERMINGAL_GROUPS_IDS_RAW = requests.post(url=terminals_url, headers=headers, data=json.dumps(data)).json()['terminalGroups']
print(TERMINGAL_GROUPS_IDS_RAW)

change_payments_url = 'https://api-eu.iiko.services/api/1/deliveries/change_payments'

data = {
    "organizationId": "b9eede12-44d1-4eaf-9724-1fa9237be4da",
    "orderId": "99fed126-196b-4595-8b55-470b0cbabf55",
    "payments": [
        {
            "paymentTypeKind": "Cash",
            "sum": 8.55,
            "paymentTypeId": "09322f46-578a-d210-add7-eec222a08871",
            # "isProcessedExternally": true,
            # "paymentAdditionalData": {},
            # "isFiscalizedExternally": true
        }
    ],
    "tips": [
    {
        'paymentTypeKind': 'Cash',
        'tipsTypeId': '0ef8fb9a-57aa-f746-0181-908bfcb8529b',
        'sum': 21,
        'paymentTypeId': '09322f46-578a-d210-add7-eec222a08871'

    }
    ]
}
CHANGE_PAYMENTS = requests.post(url=change_payments_url, headers=headers, data=json.dumps(data)).json()

print(CHANGE_PAYMENTS)