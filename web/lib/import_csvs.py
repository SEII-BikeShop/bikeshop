from web.models import *
from dateutil import parser
import csv

tables = [
    Component
    # City, Modeltype, Paint, Letterstyle, Retailstore, Customer, Customertransaction,
    # Employee, Tubematerial, Manufacturer, Letterstyle, Componentname, Component,
    # Bikeparts, Biketubes, Commonsizes, Groupcomponents, Groupo,
    # Manufacturertransaction, Modelsize, Preference, Purchaseitem, Purchaseorder,
    # Revisionhistory, Samplename, Samplestreet, Statetaxrate, Tempdatemade,
    # Workarea, Bicycletubeusage, Bicycle
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
                if 'date' in key:
                    try:
                        record[key] = parser.parse(value)
                    except:
                        pass

                # General
                if key.endswith('id') and table.__name__.lower() + 'id' != key:
                    record[key + '_id'] = value
                    del record[key]
                if key.endswith('type') and represents_int(value):
                    record[key + '_id'] = value
                    del record[key]
                if value == '':
                    record[key] = None

                # One-off uses
                # if key == 'category' and table == Component:
                #     record[key] = Component.objects.get(componentname=value)

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
