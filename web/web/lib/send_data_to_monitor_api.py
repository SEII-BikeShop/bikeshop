import requests
import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USERNAME = 'team_db'
PASSWORD = 'password'
TOKEN = '123d46bbe98753eb707ed6dc66e97979'

# If you don't already have an account
def create_account():
    url = 'http://bikeshopmonitoring.duckdns.org/Admin/Create'.format(id)
    data = {
        "Admin": {
            "FirstName": 'First',
            "LastName": 'Last',
            "MiddleName": 'Middle',
            "Email": 'db_team@example.com',
            "UserName": USERNAME
        },
        "Password": PASSWORD
    }
    data = requests.post(url, data = data, verify=False, headers={"Content-Type":"application/json"})
    print(data)
# create_account()

def get_account_token():
    url = 'https://bikeshopmonitoring.duckdns.org/Admin/Login/'
    data = { 'UserName': USERNAME, 'Password': PASSWORD }
    result = requests.post(url, data = data, verify=False, headers={"Content-Type":"application/json"})
    print(result)
# get_account_token()
