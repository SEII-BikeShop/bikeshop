from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
import requests

from django.core import serializers
import json

def index(request):
    bikes = []
    if request.session.get('bikes', False):
        bikes = request.session.get('bikes')
    else:
        url = 'http://127.0.0.1:8080/api/v0/bicycle/?format=json'
        filter = {'key': 'value'}
        bikes = requests.get(url, data = filter)
        bikes = bikes.json()

        print(bikes)

        request.session['bikes'] = bikes

    if request.session.get('account', False):
        print('LOGGED IN')
        data = request.session.get('account', False)
        data['override_base'] = 'layout_account.html'
        data['bikes'] = bikes

        return render(request, 'index.html', data)
    else:
        # Cookie is not set
        print('NOT LOGGED IN')
        return render(request, 'index.html', { 'bikes': bikes })
        # return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            if form.is_valid():
                url = 'http://127.0.0.1:8080/api/v0/users/?format=json'
                filter = {'key': 'value'}
                data = requests.get(url, data = filter)

                print(json.loads(data.text)[0])

                data = json.loads(data.text)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                try:
                    user = next(item for item in data if item["username"] == username and item["password"] == password)
                    print('YES USER')
                    print(user)

                    request.session['account'] = user

                    return HttpResponseRedirect('index')
                except Exception:
                    print('NO USER')
                    return render(request, 'login.html', {'form': form, 'error': 'ERROR: Incorrect username / password combo'})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    del request.session['account']
    return HttpResponseRedirect('index')
