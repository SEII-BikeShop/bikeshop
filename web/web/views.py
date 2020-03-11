from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, SearchForm
import requests

from django.core import serializers
import json

def index(request):
    url = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        if form.is_valid():

            print(form.cleaned_data['search'])

            search = form.cleaned_data['search']
            url = 'http://127.0.0.1:8080/api/v0/bicycle/?format=json&limit=120&offset=1&?search={}'.format(
                search
            )
    else:
        form = SearchForm()
        url = 'http://127.0.0.1:8080/api/v0/bicycle/?format=json&limit=120&offset=1'

    filter = {'key': 'value'}
    bikes = requests.get(url, data = filter)
    bikes = bikes.json()['results']

    # print(bikes[0])

    if request.session.get('account', False):
        print('LOGGED IN')
        data = request.session.get('account', False)

        print(data)

        data['override_base'] = 'layout_account.html'
        data['logged_in'] = True
        data['bikes'] = bikes
        data['form'] = form

        return render(request, 'index.html', data)
    else:
        # Cookie is not set
        print('NOT LOGGED IN')
        return render(request, 'index.html', { 'form': form, 'bikes': bikes })

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

def delete_bike(request, id):
    url = 'http://127.0.0.1:8080/api/v0/bicycle/{}?format=json'.format(id)
    filter = {}
    bikes = requests.delete(url, data = filter)

    return HttpResponseRedirect('/index')
