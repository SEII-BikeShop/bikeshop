from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import *
from dateutil import parser
import csv

class EndpointTestCase(APITestCase):

    # def setup(self):
    #     import_test_data = ImportTestData()
    #     import_test_data.import_data(max_records_per_table = 5)

    def test_get_user(self):
        Users.objects.get_or_create(
            id=1, username='customer', usertype='customer', usertypeid=1
        )

        data = {}
        url = 'http://127.0.0.1:8080/api/v0/users/1/?format=json'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)





class ImportTestData:

    def __init__(self):
        self.tables = [
            City, Modeltype, Paint, Letterstyle, Retailstore, Customer, Customertransaction,
            Employee, Tubematerial, Manufacturer, Letterstyle, Componentname, Component,
            Commonsizes, Groupo, Groupcomponents,
            Manufacturertransaction, Modelsize, Preference, Purchaseorder, Purchaseitem,
            Revisionhistory, Samplename, Samplestreet, Statetaxrate, Tempdatemade,
            Workarea, Bicycle, Bicycletubeusage, Bikeparts, Biketubes
        ]

    def represents_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def import_data(self, max_records_per_table=5):
        for table in self.tables:
            if table.objects.count() > max_records_per_table:
                break

            with open('api/lib/data/{}_DATA_TABLE.csv'.format(table.__name__.upper()), encoding="utf8", errors='ignore') as file:
                print('Creating data for table: ', table.__name__)
                reader = csv.DictReader(file)
                for record in reader:
                    if table.objects.count() > max_records_per_table:
                        break

                    record =  {k.lower(): v for k, v in record.items()}
                    for key, value in record.copy().items():
                        if table.objects.count() > max_records_per_table:
                            break

                        # General
                        if 'date' in key:
                            try:
                                record[key] = parser.parse(value)
                            except:
                                pass
                        if key.endswith('id') and table.__name__.lower() + 'id' != key and key not in ['pricepaid']:
                            record[key + '_id'] = value
                            del record[key]
                        if key.endswith('type'):
                            record[key + '_id'] = value
                            del record[key]
                        if value == '':
                            record[key] = None

                        # One-off uses
                        if key == 'category' and table == Component:
                            try:
                                record[key] = Componentname.objects.get(componentname=value)
                            except Exception as e:
                                print(e)
                        if key == 'serialnumber':
                            try:
                                record[key] = Bicycle.objects.get(serialnumber=value)
                            except Exception as e:
                                print(e)

                    # forget about foriegn key restraints
                    try:
                        table.objects.get_or_create(**record)
                    except Exception as error:
                        if 'Duplicate entry' not in str(error):
                            print('Table {}'.format(table.__name__))
                            print('Error: ', error)
                            print('Record data: ', record)
                            print('\n')
                            print('\n')
                        pass
