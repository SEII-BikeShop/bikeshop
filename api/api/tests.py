from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import *
import requests


class EndpointTestCase(APITestCase):

    def test_successfully_fail(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/random_place'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

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

    def test_get_employee(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/employee/0?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bicycle_tube_usage(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/bicycletubeusage/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_biketube(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/biketubes'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_component(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/component/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customer(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/customer/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_groupo(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/groupo/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_manufacturer(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/manufacturer/1?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_purchaseorder(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/purchaseorder/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retailstore(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/retailstore/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_revisionhistory(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/revisionhistory/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_samplename(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/samplename/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
