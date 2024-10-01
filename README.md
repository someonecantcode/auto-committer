# auto-committer

## tools:
* postman
* js

## purpose:
wanna flex to your friends your cracked skills on github? <br/> say less with this
automatic committer that will continue your contribution streak, ✨ ***forever*** 🌟.

## how this works:

* use github rest api
* go to devoloper settings and create api key with repo code read&write perms
* PUT https://api.github.com/repos/someonecantcode/auto-committer/contents/data
```json
{
    "name": "auto-committer",
    "full_name": "someonecantcode/auto-committer",
    "private": false,
    "sha": "8b137891791fe96927ad78e64b0aad7bded08bdc",
    "message": "test update",
    "content": "dGVzdGluZw=="
}
```
* sha is obtained from GET https://api.github.com/repos/someonecantcode/auto-committer/contents
* content is the string encoded in Base64
