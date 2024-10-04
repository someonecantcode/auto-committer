import requests, base64, json, os
from dotenv import load_dotenv
load_dotenv()

def getDataSHA(fileName: str) -> str:
    data_REPO = requests.get("https://api.github.com/repos/someonecantcode/auto-committer/contents").content
    for info in json.loads(data_REPO):
        if(info['name'] == fileName):
            return info['sha']
def updateFile(data: str, API_KEY: str) -> requests.Response:
    content = base64.b64encode(bytes(data, 'utf-8')).decode('utf-8')
    payload = {
    "name": "auto-committer",
    "full_name": "someonecantcode/auto-committer",
    "sha": getDataSHA("data"),
    "message": "test update1",
    "content": content
    }
    return requests.put('https://api.github.com/repos/someonecantcode/auto-committer/contents/data', auth=("someonecantcode", API_KEY), data=json.dumps(payload))

API_KEY: str = os.getenv("API_KEY")
msg: str = "day 2 of testing"

r = updateFile(msg, API_KEY)
# print(json.loads(r.content))
# print(r.status_code)