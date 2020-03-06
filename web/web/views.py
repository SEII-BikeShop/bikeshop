from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
import requests

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            if form.is_valid():
                # print(form.cleaned_data['username'])

                url = 'http://127.0.0.1:8080/api/v0/city/?format=json'
                filter = {'key': 'value'}

                data = requests.get(url, data = filter)

                print(data.text)


                return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
