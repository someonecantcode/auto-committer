import requests, base64
import json, os, random, time

def getDataSHA(fileName: str) -> str:
    data_REPO = requests.get("https://api.github.com/repos/someonecantcode/auto-committer/contents").content
    for info in json.loads(data_REPO):
        if(info['name'] == fileName):
            return info['sha']
def updateFile(data: str, msg: str, API_KEY: str) -> requests.Response:
    content = base64.b64encode(bytes(data, 'utf-8')).decode('utf-8')
    payload = {
    "name": "auto-committer",
    "full_name": "someonecantcode/auto-committer",
    "sha": getDataSHA("data"),
    "message": msg,
    "content": content
    }
    return requests.put('https://api.github.com/repos/someonecantcode/auto-committer/contents/data', auth=("someonecantcode", API_KEY), data=json.dumps(payload))

random.seed(time.time())
API_KEY: str = os.environ["API_KEY"]
content: str =  os.environ["ORIGINAL_MSG"] +"\n" + str(random.random()) 
msg: str = "hip hip horay"

r = updateFile(content, msg, API_KEY)
print(r.status_code)
# print(json.loads(r.content))
