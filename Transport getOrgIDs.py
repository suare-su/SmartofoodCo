import requests
import json

headers = {'Content-Type': 'application/json'}
data = {
    "apiLogin": "bb58474a"
}
data = json.dumps(data)
a = requests.post("https://api-ru.iiko.services/api/1/access_token", data = data, headers = headers)

print(a.json())

#{'correlationId': 'c8ff98d7-8e8f-463a-8d7f-90d97e893c29', 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiN2QxZTZhYTgtNWYyNC00MzlkLTg3OWEtYWQ0MDgyNmI2ZTkyIiwibmJmIjoxNjQyNTc1MDUwLCJleHAiOjE2NDI1Nzg2NTAsImlhdCI6MTY0MjU3NTA1MCwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.ofWjPd-hK0CkTvtMSvnEix-7R0SGVJn_BIVNUdIK-bM'}

TOKEN = a.json()['token']

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN}
data = {}
data = json.dumps(data)
b = requests.post("https://api-ru.iiko.services/api/1/organizations", data = data, headers = headers)
print(b.json())

