from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import *
import requests

class Bike:
    def create(self):
        data = {
            "serialnumber": "191919191",
            "framesize": 52.0,
            "orderdate": "1994-01-12T00:00:00",
            "startdate": "1994-01-13T00:00:00",
            "shipdate": "1994-01-20T00:00:00",
            "shipemployee": "15293",
            "frameassembler": "89097",
            "painter": "12512",
            "construction": "TIG Welded",
            "waterbottlebrazeons": "4",
            "customname": "Lisa Bronson",
            "toptube": 53.0,
            "chainstay": 41.5,
            "headtubeangle": 73.0,
            "seattubeangle": 73.5,
            "listprice": "2066.2700",
            "saleprice": "1333.3300",
            "salestax": "0.0000",
            "salestate": "NE",
            "shipprice": "70.0000",
            "frameprice": "398.7000",
            "componentlist": "1250.0000",
            "customerid": 1.0,
            "modeltype": "Road",
            "paintid": 6.0,
            "letterstyleid": "Script",
            "storeid": 3098.0,
            "employeeid": 34192.0
        }
        url = 'http://127.0.0.1:8080/api/v0/bicycle/'
        response = requests.post(url, data = data)
        return response


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

    def test_get_samplestreet(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/samplestreet/2?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tubematerial(self):
        data = {}
        url = 'http://127.0.0.1:8080/api/v0/tubematerial/220?format=json'
        response = requests.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_bike(self):
        bike = Bike()
        response = bike.create()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bike.delete()
