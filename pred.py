import requests
import json

url = "http://localhost:8000/predict?text=mohan"
# data = {"text":"mohan"}
# data = json.dumps(data)
headers = {"Content-Type": "application/json","access-control-allow-credentials": "true"}
resp = requests.post(url=url,headers=headers)

print(resp.content)