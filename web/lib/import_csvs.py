from web.models import *
from dateutil import parser
import csv

tables = [
    City, Modeltype, Paint, Letterstyle, Retailstore, Customer, Customertransaction,
    Employee, Tubematerial, Manufacturer, Letterstyle, Componentname, Component,
    Commonsizes, Groupo, Groupcomponents,
    Manufacturertransaction, Modelsize, Preference, Purchaseorder, Purchaseitem,
    Revisionhistory, Samplename, Samplestreet, Statetaxrate, Tempdatemade,
    Workarea, Bicycle, Bicycletubeusage, Bikeparts, Biketubes
]

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

for table in tables:
     with open('web/lib/data/{}_DATA_TABLE.csv'.format(table.__name__.upper()), encoding="utf8", errors='ignore') as file:
        print('Creating data for table: ', table.__name__)
        reader = csv.DictReader(file)
        for record in reader:
            record =  {k.lower(): v for k, v in record.items()}
            for key, value in record.copy().items():
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
