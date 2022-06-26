import json
import requests
#TOKEN = requests.get('https://iiko.biz:9900/api/0/auth/access_token?user_id=interlab@mail.ru&user_secret=VMOB9sQYNS0RO6vOugzs').json()
TOKEN = requests.get('https://iiko.biz:9900/api/0/auth/access_token?user_id=smartofood_biz&user_secret=smarTofood_p@ss13').json()
print(TOKEN)
orgID = requests.get('https://iiko.biz:9900/api/0/organization/list?access_token=%s' % TOKEN).json()
print(orgID)
orgID = '10415b0f-e933-11e6-80ca-d8d385655247'
orgID = '5f850000-90a3-0025-0bec-08d941dcf040'
nomenclature = requests.get('https://iiko.biz:9900/api/0/nomenclature/%s?access_token=%s' % (orgID, TOKEN)).json() #вся номенклатура
print(json.dumps(nomenclature))
# orderTypes = requests.get('https://iiko.biz:9900/api/0/rmsSettings/getOrderTypes?organization=%s&access_token=%s' % (orgID, TOKEN)).json() #вся номенклатура
# print(orderTypes)