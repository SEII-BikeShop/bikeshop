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

def send_bike_data(bike, token):
    url = 'https://bikeshopmonitoring.duckdns.org/Bike/Create'
    data = {
        "Name": bike['serialnumber'] + "' " + bike['modeltype'],
        "SalesPrice": float(bike['saleprice'])
    }
    print(json.dumps(data))
    result = requests.post(url, data = json.dumps(data), verify=False, headers={
        "Token": token, "Content-Type": "application/json"
    })
    print(result)
    print('\n')

def get_bike_data():
    offset = 1

    token = TOKEN

    while True:
        url = 'http://127.0.0.1:8080/api/v0/bicycle/?format=json&limit=20&offset={}'.format(offset)
        bikes = requests.get(url)
        bikes = bikes.json()['results']

        if bikes == []:
            return None

        for bike in bikes:
            send_bike_data(bike, token)
        offset += 1
get_bike_data()
