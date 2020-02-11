# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False
#   * managed = False
# lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bicycle(models.Model):
    serialnumber = models.DecimalField(db_column='SERIALNUMBER', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    customerid = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CUSTOMERID', blank=True, null=True)  # Field name made lowercase.
    modeltype = models.ForeignKey('Modeltype', models.DO_NOTHING, db_column='MODELTYPE', blank=True, null=True)  # Field name made lowercase.
    paintid = models.ForeignKey('Paint', models.DO_NOTHING, db_column='PAINTID', blank=True, null=True)  # Field name made lowercase.
    framesize = models.FloatField(db_column='FRAMESIZE', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='ORDERDATE', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    shipdate = models.DateTimeField(db_column='SHIPDATE', blank=True, null=True)  # Field name made lowercase.
    shipemployee = models.DecimalField(db_column='SHIPEMPLOYEE', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    frameassembler = models.DecimalField(db_column='FRAMEASSEMBLER', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    painter = models.DecimalField(db_column='PAINTER', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    construction = models.CharField(db_column='CONSTRUCTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    waterbottlebrazeons = models.DecimalField(db_column='WATERBOTTLEBRAZEONS', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    customname = models.CharField(db_column='CUSTOMNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    letterstyleid = models.ForeignKey('Letterstyle', models.DO_NOTHING, db_column='LETTERSTYLEID', blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Retailstore', models.DO_NOTHING, db_column='STOREID', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EMPLOYEEID', blank=True, null=True)  # Field name made lowercase.
    toptube = models.FloatField(db_column='TOPTUBE', blank=True, null=True)  # Field name made lowercase.
    chainstay = models.FloatField(db_column='CHAINSTAY', blank=True, null=True)  # Field name made lowercase.
    headtubeangle = models.FloatField(db_column='HEADTUBEANGLE', blank=True, null=True)  # Field name made lowercase.
    seattubeangle = models.FloatField(db_column='SEATTUBEANGLE', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='LISTPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SALEPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salestax = models.DecimalField(db_column='SALESTAX', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salestate = models.CharField(db_column='SALESTATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipprice = models.DecimalField(db_column='SHIPPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frameprice = models.DecimalField(db_column='FRAMEPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    componentlist = models.DecimalField(db_column='COMPONENTLIST', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'BICYCLE'


class Bicycletubeusage(models.Model):
    serialnumber = models.OneToOneField(Bicycle, models.DO_NOTHING, db_column='SERIALNUMBER', primary_key=True)  # Field name made lowercase.
    tubeid = models.ForeignKey('Tubematerial', models.DO_NOTHING, db_column='TUBEID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'BICYCLETUBEUSAGE'
        unique_together = (('serialnumber', 'tubeid'), ('serialnumber', 'tubeid'),)


class Bikeparts(models.Model):
    serialnumber = models.OneToOneField(Bicycle, models.DO_NOTHING, db_column='SERIALNUMBER', primary_key=True)  # Field name made lowercase.
    componentid = models.ForeignKey('Component', models.DO_NOTHING, db_column='COMPONENTID')  # Field name made lowercase.
    substituteidentifer = models.DecimalField(db_column='SUBSTITUTEID', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='QUANTITY', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dateinstalled = models.DateTimeField(db_column='DATEINSTALLED', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EMPLOYEEID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'BIKEPARTS'
        unique_together = (('serialnumber', 'componentid'), ('serialnumber', 'componentid'),)


class Biketubes(models.Model):
    serialnumber = models.OneToOneField(Bicycle, models.DO_NOTHING, db_column='SERIALNUMBER', primary_key=True)  # Field name made lowercase.
    tubename = models.CharField(db_column='TUBENAME', max_length=50)  # Field name made lowercase.
    tubeid = models.ForeignKey('Tubematerial', models.DO_NOTHING, db_column='TUBEID', blank=True, null=True)  # Field name made lowercase.
    length = models.FloatField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'BIKETUBES'
        unique_together = (('serialnumber', 'tubename'), ('serialnumber', 'tubename'),)


class City(models.Model):
    cityid = models.DecimalField(db_column='CITYID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AREACODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    population1990 = models.DecimalField(db_column='POPULATION1990', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    population1980 = models.DecimalField(db_column='POPULATION1980', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True, default=0)  # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True, default=0)  # Field name made lowercase.
    populationcdf = models.FloatField(db_column='POPULATIONCDF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'CITY'


class Commonsizes(models.Model):
    modeltype = models.CharField(db_column='MODELTYPE', primary_key=True, max_length=50)  # Field name made lowercase.
    framesize = models.FloatField(db_column='FRAMESIZE')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'COMMONSIZES'
        unique_together = (('modeltype', 'framesize'), ('modeltype', 'framesize'),)


class Component(models.Model):
    componentid = models.DecimalField(db_column='COMPONENTID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    manufacturerid = models.ForeignKey('Manufacturer', models.DO_NOTHING, db_column='MANUFACTURERID', blank=True, null=True)  # Field name made lowercase.
    productnumber = models.CharField(db_column='PRODUCTNUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    road = models.CharField(db_column='ROAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('Componentname', models.DO_NOTHING, db_column='CATEGORY', blank=True, null=True)  # Field name made lowercase.
    length = models.FloatField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    width = models.FloatField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    year = models.DecimalField(db_column='YEAR', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    endyear = models.DecimalField(db_column='ENDYEAR', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='LISTPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estimatedcost = models.DecimalField(db_column='ESTIMATEDCOST', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantityonhand = models.FloatField(db_column='QUANTITYONHAND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'COMPONENT'


class Componentname(models.Model):
    componentname = models.CharField(db_column='COMPONENTNAME', primary_key=True, max_length=50)  # Field name made lowercase.
    assemblyorder = models.DecimalField(db_column='ASSEMBLYORDER', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'COMPONENTNAME'


class Customer(models.Model):
    customerid = models.DecimalField(db_column='CUSTOMERID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CITYID', blank=True, null=True)  # Field name made lowercase.
    balancedue = models.DecimalField(db_column='BALANCEDUE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'CUSTOMER'



class Employee(models.Model):
    employeeid = models.DecimalField(db_column='EMPLOYEEID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    taxpayeridentifier = models.CharField(db_column='TAXPAYERID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HOMEPHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CITYID', blank=True, null=True)  # Field name made lowercase.
    datehired = models.DateTimeField(db_column='DATEHIRED', blank=True, null=True)  # Field name made lowercase.
    datereleased = models.DateTimeField(db_column='DATERELEASED', blank=True, null=True)  # Field name made lowercase.
    currentmanager = models.DecimalField(db_column='CURRENTMANAGER', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarygrade = models.DecimalField(db_column='SALARYGRADE', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='SALARY', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    workarea = models.CharField(db_column='WORKAREA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'EMPLOYEE'


class Customertransaction(models.Model):
    customerid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='CUSTOMERID', primary_key=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TRANSACTIONDATE')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EMPLOYEEID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    reference = models.DecimalField(db_column='REFERENCE', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'CUSTOMERTRANSACTION'
        unique_together = (('customerid', 'transactiondate'), ('customerid', 'transactiondate'),)



class Groupcomponents(models.Model):
    groupid = models.OneToOneField('Groupo', models.DO_NOTHING, db_column='GROUPID', primary_key=True)  # Field name made lowercase.
    componentid = models.ForeignKey(Component, models.DO_NOTHING, db_column='COMPONENTID')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'GROUPCOMPONENTS'
        unique_together = (('groupid', 'componentid'), ('groupid', 'componentid'),)


class Groupo(models.Model):
    groupoid = models.DecimalField(db_column='COMPONENTGROUPID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    groupname = models.CharField(db_column='GROUPNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    biketype = models.CharField(db_column='BIKETYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.DecimalField(db_column='YEAR', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    endyear = models.DecimalField(db_column='ENDYEAR', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='WEIGHT', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'GROUPO'


class Letterstyle(models.Model):
    letterstyle = models.CharField(db_column='LETTERSTYLE', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'LETTERSTYLE'


class Manufacturer(models.Model):
    manufacturerid = models.DecimalField(db_column='MANUFACTURERID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    manufacturername = models.CharField(db_column='MANUFACTURERNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='CONTACTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CITYID', blank=True, null=True)  # Field name made lowercase.
    balancedue = models.DecimalField(db_column='BALANCEDUE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'MANUFACTURER'


class Manufacturertransaction(models.Model):
    manufacturerid = models.OneToOneField(Manufacturer, models.DO_NOTHING, db_column='MANUFACTURERID', primary_key=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TRANSACTIONDATE')  # Field name made lowercase.
    employee = models.DecimalField(db_column='EMPLOYEEID', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    reference = models.DecimalField(db_column='REFERENCE', max_digits=38, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'MANUFACTURERTRANSACTION'
        unique_together = (('manufacturerid', 'transactiondate', 'reference'), ('manufacturerid', 'transactiondate', 'reference'),)


class Modelsize(models.Model):
    modeltype = models.OneToOneField('Modeltype', models.DO_NOTHING, db_column='MODELTYPE', primary_key=True)  # Field name made lowercase.
    msize = models.FloatField(db_column='MSIZE')  # Field name made lowercase.
    toptube = models.FloatField(db_column='TOPTUBE', blank=True, null=True)  # Field name made lowercase.
    chainstay = models.FloatField(db_column='CHAINSTAY', blank=True, null=True)  # Field name made lowercase.
    totallength = models.FloatField(db_column='TOTALLENGTH', blank=True, null=True)  # Field name made lowercase.
    groundclearance = models.FloatField(db_column='GROUNDCLEARANCE', blank=True, null=True)  # Field name made lowercase.
    headtubeangle = models.FloatField(db_column='HEADTUBEANGLE', blank=True, null=True)  # Field name made lowercase.
    seattubeangle = models.FloatField(db_column='SEATTUBEANGLE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'MODELSIZE'
        unique_together = (('modeltype', 'msize'), ('modeltype', 'msize'),)


class Modeltype(models.Model):
    modeltype = models.CharField(db_column='MODELTYPE', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    componentid = models.DecimalField(db_column='COMPONENTID', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'MODELTYPE'


class Paint(models.Model):
    paintid = models.DecimalField(db_column='PAINTID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    colorname = models.CharField(db_column='COLORNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colorstyle = models.CharField(db_column='COLORSTYLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    colorlist = models.CharField(db_column='COLORLIST', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateintroduced = models.DateTimeField(db_column='DATEINTRODUCED', blank=True, null=True)  # Field name made lowercase.
    datediscontinued = models.DateTimeField(db_column='DATEDISCONTINUED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'PAINT'


class Preference(models.Model):
    itemname = models.CharField(db_column='ITEMNAME', primary_key=True, max_length=50)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    datechanged = models.DateTimeField(db_column='DATECHANGED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'PREFERENCE'


class Purchaseitem(models.Model):
    purchaseid = models.OneToOneField('Purchaseorder', models.DO_NOTHING, db_column='PURCHASEID', primary_key=True)  # Field name made lowercase.
    componentid = models.ForeignKey(Component, models.DO_NOTHING, db_column='COMPONENTID')  # Field name made lowercase.
    pricepaid = models.DecimalField(db_column='PRICEPAID', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='QUANTITY', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    quantityreceived = models.DecimalField(db_column='QUANTITYRECEIVED', max_digits=38, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'PURCHASEITEM'
        unique_together = (('purchaseid', 'componentid'), ('purchaseid', 'componentid'),)


class Purchaseorder(models.Model):
    purchaseorderid = models.DecimalField(db_column='PURCHASEID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EMPLOYEEID', blank=True, null=True)  # Field name made lowercase.
    manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='MANUFACTURERID', blank=True, null=True)  # Field name made lowercase.
    totallist = models.DecimalField(db_column='TOTALLIST', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    shippingcost = models.DecimalField(db_column='SHIPPINGCOST', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='ORDERDATE', blank=True, null=True)  # Field name made lowercase.
    receivedate = models.DateTimeField(db_column='RECEIVEDATE', blank=True, null=True)  # Field name made lowercase.
    amountdue = models.DecimalField(db_column='AMOUNTDUE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'PURCHASEORDER'


class Retailstore(models.Model):
    retailstoreid = models.DecimalField(db_column='STOREID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    storename = models.CharField(db_column='STORENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='CONTACTFIRSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactlastname = models.CharField(db_column='CONTACTLASTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZIPCODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CITYID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'RETAILSTORE'


class Revisionhistory(models.Model):
    revisionhistoryid = models.DecimalField(db_column='ID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='CHANGEDATE', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    revisioncomments = models.CharField(db_column='REVISIONCOMMENTS', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'REVISIONHISTORY'


class Samplename(models.Model):
    samplenameid = models.DecimalField(db_column='ID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'SAMPLENAME'


class Samplestreet(models.Model):
    samplestreetid = models.DecimalField(db_column='ID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    baseaddress = models.CharField(db_column='BASEADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'SAMPLESTREET'


class Statetaxrate(models.Model):
    state = models.CharField(db_column='STATE', primary_key=True, max_length=50)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TAXRATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'STATETAXRATE'


class Tempdatemade(models.Model):
    datevalue = models.DateTimeField(db_column='DATEVALUE', primary_key=True)  # Field name made lowercase.
    madecount = models.FloatField(db_column='MADECOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'TEMPDATEMADE'


class Tubematerial(models.Model):
    tubematerialid = models.DecimalField(db_column='TUBEID', primary_key=True, max_digits=38, decimal_places=0)  # Field name made lowercase.
    material = models.CharField(db_column='MATERIAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diameter = models.FloatField(db_column='DIAMETER', blank=True, null=True)  # Field name made lowercase.
    thickness = models.FloatField(db_column='THICKNESS', blank=True, null=True)  # Field name made lowercase.
    roundness = models.CharField(db_column='ROUNDNESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    stiffness = models.FloatField(db_column='STIFFNESS', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='LISTPRICE', max_digits=38, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    construction = models.CharField(db_column='CONSTRUCTION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'TUBEMATERIAL'


class Workarea(models.Model):
    workarea = models.CharField(db_column='WORKAREA', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'bikeshop_web'
        db_table = 'WORKAREA'
