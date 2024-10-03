import requests
import base64
import json
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()



API_KEY = os.getenv("API_KEY")

data = "hello world!"
content = base64.b64encode(bytes(data, 'utf-8')).decode('utf-8')

data_REPO = requests.get("https://api.github.com/repos/someonecantcode/auto-committer/contents").content
data_SHA = ''
for info in json.loads(data_REPO):
    if(info['name'] == "data"):
        data_SHA = info['sha']
        break



payload = {
    "name": "auto-committer",
    "full_name": "someonecantcode/auto-committer",
    "sha": data_SHA,
    "message": "test update1",
    "content": content
}

r = requests.put('https://api.github.com/repos/someonecantcode/auto-committer/contents/data', auth=("someonecantcode", API_KEY), data=json.dumps(payload))
# print(r.content)
# print(r.json)
# print(r.status_code)