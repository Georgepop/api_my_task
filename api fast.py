
import requests
import json

imput = {"command" : 'ON',
"metadata" : 'YELLOW'}

j_data = json.dumps(imput)
headers = {'Content-Type': 'application/json'}
r = requests.post('http://127.0.0.1:5000/score', data=j_data, headers=headers)
print(r)