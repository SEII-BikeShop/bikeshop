from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
import requests

def create_admin(request):
    #somecode
    admin_info = {
        "Admin": {
            "FirstName": "Austin",
            "LastName": "Lee",
            "Middle": "Johnathan",
            "Email": "LEEAJ1@ETSU.EDU",
            "UserName": "alee"
        },
        "Password": "password"
    }
    r = requests.post('https://bikeshopmonitoring.duckdns.org/Admin/Create', data=admin_info)
    if r.status_code == 200:
        print(r)

def send_data():
    print("hello")
