from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import *
from dateutil import parser
import requests
import csv


class EndpointTestCase(APITestCase):

    def test_get_user(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/users/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bicycle(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/bicycle/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_city(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/city/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_paint(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/paint/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
