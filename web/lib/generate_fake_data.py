# ImportUse exit() or Ctrl-D (i.e. EOF) to exit
from web.models import *
from faker import Faker
fake = Faker()
import random

# -- Create City Data --
CITY_NUM = City.objects.all().count()
CITY_TO_CREATE = 100

if CITY_NUM < CITY_TO_CREATE:
    for index in range(0, CITY_TO_CREATE):
        population1980 = random.randint(40000,300000)
        population1990 = population1980 + random.randint(10000, 50000)
        populationcdf  = population1990 + random.randint(0, 100000)

        city_id = 0
        if City.objects.all().count() >= 1:
            city_id = City.objects.latest('cityid').cityid + 1

        city = City(
            cityid = city_id,
            zipcode = fake.zipcode(),
            city = fake.city(),
            state = fake.state(),
            areacode = fake.postalcode(),
            population1980 = population1980,
            population1990 = population1990,
            country = fake.country(),
            latitude = fake.latitude(),
            longitude = fake.longitude(),
            populationcdf = populationcdf
        )
        city.save()
