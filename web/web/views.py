from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, SearchForm, EditForm
import requests

from django.core import serializers
import json

def index(request):
    url = 'http://127.0.0.1:8080/api/v0/bicycle/?format=json&limit=120&offset=1'
    filter = {'key': 'value'}
    bikes = requests.get(url, data = filter)
    bikes = bikes.json()['results']

    print(bikes[0])

    if request.session.get('account', False):
        print('LOGGED IN')
        data = request.session.get('account', False)

        print(data)

        data['override_base'] = 'layout_account.html'
        data['logged_in'] = True
        data['bikes'] = bikes

        return render(request, 'index.html', data)
    else:
        # Cookie is not set
        print('NOT LOGGED IN')
        return render(request, 'index.html', { 'bikes': bikes })

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

def update_bike(request, id):
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = EditForm(request.POST)
            if form.is_valid():
                try:
                    url = 'http://127.0.0.1:8080/api/v0/bicycle/{}/'.format(id)
                    data = form.cleaned_data
                    result = requests.patch(url, data = data)

                    print(result)

                    return HttpResponseRedirect('/index')
                except Exception:
                    print('NO USER')
                    return render(request, 'edit.html', {'form': form, 'error': 'ERROR: Data is invalid'})
    # if a GET (or any other method) we'll create a blank form
    else:
        url = 'http://127.0.0.1:8080/api/v0/bicycle/{}?format=json'.format(id)
        data = requests.get(url)
        parsed_data = json.loads(data.text)
        form = EditForm(initial=parsed_data)

    return render(request, 'edit.html', {'form': form})

def add_bike(request):
    # create a form instance and populate it with data from the request:
    form = BicycleForm(request.POST)
    if form.is_valid():
        try:
            bike = form.cleaned_data
            bike.save()
            print(bike)
            return HttpResponseRedirect('/index')
        except Exception:
            print('Adding error')
            return render(request, 'add_bike.html', {'form': form, 'error': 'ERROR: Data is invalid'})

    return render(request, 'add_bike.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     url = 'http://127.0.0.1:8080/api/v0/bicycle/{}?format=json'.format(id)
    #     data = requests.get(url)
    #     parsed_data = json.loads(data.text)
    #     form = EditForm(initial=parsed_data)

    # f = CreateForm(request.POST)
    # bike = f.cleaned_data
    # bike.save()


    # if request.method == 'POST':
    #     form = CreateForm(request.POST)
    #     if form.is_valid():
    #         modeltype = form.cleaned_data['modeltype']
    #         listprice = form.cleaned_data['listprice']
    #         construction = form.cleaned_data['construction']
    #         letterstyleid = form.cleaned_data['letterstyleid']
    #         framesize = form.cleaned_data['framesize']
    #         toptube = form.cleaned_data['toptube']
    #         chainstay = form.cleaned_data['chainstay']
    #         headtubeangle = form.cleaned_data['headtubeangle']
    #         seattubeangle = form.cleaned_data['seattubeangle']
    #         query = Bicycle(modeltype = modeltype, listprice = listprice,
    #             construction = construction, letterstyleid = letterstyleid,
    #             framesize = framesize, toptube = toptube,
    #             chainstay = chainstay, headtubeangle = headtubeangle,
    #             seattubeangle = seattubeangle)
    #         query.save()
    # return render(request, 'add_bike.html', {'form': form})

def create_admin(request):
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
