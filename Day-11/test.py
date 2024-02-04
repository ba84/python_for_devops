import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()

for x in range(len(complete_detail)):
    print(complete_detail[x]['requested_reviewers'][0]['login'])