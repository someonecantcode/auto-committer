<h3 align="center">auto-committer</h3>

***
![Static Badge](https://img.shields.io/badge/Python-000?logo=Python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white) </br>



## tools:
* postman
* github rest api
* python 

## purpose:
wanna flex to your friends your cracked skills on github? <br/> say less with this
automatic committer that will continue your contribution streak, ✨ ***forever*** 🌟.


## Setup
* go to devoloper settings and **create api key** with repo code read&write perms

github secrets
* go to repo's setting tab.
* in security -> secrets & variables -> actions
* create 2 repo secrets. Make sure they're named this or change the code to the name you want it to.
</br> here's how it should look like:
```
API_KEY = "the api key you just create"
ORIGINAL_MSG = "optional if you want"
```

## how this works:

using github workflow with cron, it runs the python commiter file that
updates the data file and pushes it hence commiting and updating the repo.

### github rest api
* PUT https://api.github.com/repos/someonecantcode/auto-committer/contents/data
```json
{
    "name": "auto-committer",
    "full_name": "someonecantcode/auto-committer",
    "private": false,
    "sha": "8b137891791fe96927ad78e64b0aad7bded08bdc",
    "message": "test update",
    "content": "bmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA="
}
```
* sha is obtained from GET https://api.github.com/repos/someonecantcode/auto-committer/contents
* content is the string encoded in Base64

you can test and play with its api in postman.

## testing
* go to repo's actions tab
* then go to workflow DailyPusher and you can manually trigger the workflow_dispatch trigger.
