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
#{"correlationId": "e89a50aa-52a4-42f7-8766-8c29af865ea7",
# "paymentTypes": [
# {"id": "09322f46-578a-d210-add7-eec222a08871", "code": "CASH",
# "name": "\u041d\u0430\u043b\u0438\u0447\u043d\u044b\u0435", "comment": "",
# "combinable": true, "externalRevision": 952, "applicableMarketingCampaigns": [],
# "isDeleted": false, "printCheque": true, "paymentProcessingType": "Both",
# "paymentTypeKind": "Cash", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]},
# {"id": "7c4d61bf-1841-4dc9-a08c-ca832ba33c8e", "code": "WOW", "name": "\u0410\u0433\u0440\u0435\u0433\u0430\u0442\u043e\u0440\u044b (\u0442\u0435\u0441\u0442)", "comment": "", "combinable": false, "externalRevision": 92986, "applicableMarketingCampaigns": [], "isDeleted": false, "printCheque": false, "paymentProcessingType": "Internal", "paymentTypeKind": "Card", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]},
# {"id": "80a331f4-7c39-4a03-b077-f226af718d4b", "code": "IICRD", "name": "iikoCard", "comment": "", "combinable": true, "externalRevision": 573, "applicableMarketingCampaigns": ["01330000-6bec-ac1f-eec4-08da5ad5baa0", "01330000-6bec-ac1f-9c41-08da47d69417"], "isDeleted": false, "printCheque": false, "paymentProcessingType": "Internal", "paymentTypeKind": "IikoCard", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]},
# {"id": "9d32f938-bcda-40e8-84a3-25e05a3ed30d", "code": "SBFD", "name": "SberFood", "comment": "", "combinable": true, "externalRevision": 86022, "applicableMarketingCampaigns": [], "isDeleted": true, "printCheque": false, "paymentProcessingType": "Both", "paymentTypeKind": "Unknown", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]},
# {"id": "b4fac182-de21-47fc-a0c0-5a6a69de86fc", "code": "SITE", "name": "\u041a\u0430\u0440\u0442\u043e\u0439 \u043d\u0430 \u0441\u0430\u0439\u0442\u0435", "comment": "", "combinable": true, "externalRevision": 956, "applicableMarketingCampaigns": [], "isDeleted": false, "printCheque": true, "paymentProcessingType": "External", "paymentTypeKind": "Card", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]},
# {"id": "e46b4e6c-10d5-a739-8fb1-b6674d1e65e7", "code": "BANK", "name": "\u0411\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u0438\u0435 \u043a\u0430\u0440\u0442\u044b", "comment": "", "combinable": true, "externalRevision": 955, "applicableMarketingCampaigns": [], "isDeleted": false, "printCheque": true, "paymentProcessingType": "Both", "paymentTypeKind": "Card", "terminalGroups": [{"id": "2ffb705b-d3d0-2400-017a-7ae49b7200cf", "organizationId": "2be1360a-93d0-4b17-82d4-5193a487bc3f", "name": "\u0413\u0440\u0443\u043f\u043f\u0430 \u041c\u0438\u043b\u044b\u0439 \u0431\u0430\u0440\u0441\u0443\u043a", "address": ""}]}]}

organizationId = '2be1360a-93d0-4b17-82d4-5193a487bc3f'
terminalGroupId = '2ffb705b-d3d0-2400-017a-7ae49b7200cf'
phone = "+79068755752"
tableIds = ["3be7ca30-51a0-445b-adae-4f7c013c9322"]
orderId = '70a460f2-f779-4681-8680-911dc6e9f2ce'
url = 'https://api-ru.iiko.services/api/1/order/change_payments'
data = {
    'organizationId': organizationId,
    'orderId': 'edd3d6be-1ee9-4214-8070-b8cd1d25ea2c',
   # 'posOrderIds': ['15f5025d-1dbf-431a-9a9e-3867f4cb1bfe'],
    'payments': [{
        'paymentTypeKind': 'Cash',
        'sum': 300,
        'paymentTypeId': '09322f46-578a-d210-add7-eec222a08871',
      #  'isProcessedExternally': 0,
      #  'isFiscalizedExternally': 0,

    },
        {
            'paymentTypeKind': 'Card',
            'sum': 300,
            'paymentTypeId': 'e46b4e6c-10d5-a739-8fb1-b6674d1e65e7',
            #  'isProcessedExternally': 0,
            #  'isFiscalizedExternally': 0,

        }
    ],
}
data['payments'] = [
    {
            'paymentTypeKind': 'Card',
            'sum': 400,
            'paymentTypeId': 'b4fac182-de21-47fc-a0c0-5a6a69de86fc',
            'isProcessedExternally': True,
            #  'isFiscalizedExternally': 0,

        }

]
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