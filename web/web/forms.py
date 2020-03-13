from django import forms

# from .models import Bicycle
MODELTYPES = (
    ('Hybrid', 'Hybrid'),
    ('Mountain', 'Mountain'),
    ('Mountain full', 'Mountain full'),
    ('Race', 'Race'),
    ('Road', 'Road'),
    ('Tour', 'Tour'),
    ('Track', 'Track')
)

LETTERSTYLE = (
    ('Block', 'Block'),
    ('English', 'English'),
    ('Flash', 'Flash'),
    ('Roman', 'Roman'),
    ('Script', 'Script')
)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=200)

class EditForm(forms.Form):
    modeltype = forms.ChoiceField(choices=MODELTYPES, label='Model Type')
    listprice = forms.CharField(label='List Price')
    construction = forms.CharField(label='Construction')
    letterstyleid = forms.ChoiceField(choices=LETTERSTYLE, label='Letter Style')
    framesize = forms.CharField(label='Frame Size')
    toptube = forms.CharField(label='Top Tube')
    chainstay = forms.CharField(label='Chain Stay')
    headtubeangle = forms.CharField(label='Head Tube Angle')
    seattubeangle = forms.CharField(label='Seat Tube Angle')

class CreateForm(forms.Form):
    serialnumber = forms.DecimalField(required=True, label='Serial Number')
    customerid = forms.DecimalField(required=False, label='Customer ID')
    modeltype = forms.ChoiceField(required=False, choices=MODELTYPES, label='Model Type')
    paintid = forms.DecimalField(required=False, label='Paint ID')
    framesize = forms.CharField(required=False, label='Frame Size')
    orderdate = forms.DateTimeField(required=False, label='Order Date')
    startdate = forms.DateTimeField(required=False, label='Start Date')
    shipdate = forms.DateTimeField(required=False, label='Ship Date')
    shipemployee = forms.DecimalField(required=False, label='Ship Employee')
    frameassembler = forms.DecimalField(required=False, label="Frame Assembler")
    painter = forms.DecimalField(required=False, label="Painter")
    construction = forms.CharField(required=False, label='Construction')
    waterbottlebrazeons = forms.DecimalField(required=False, label="Water Bottle Braze-ons")
    customname = forms.CharField(required=False, label="Custom Name")
    letterstyleid = forms.ChoiceField(required=False, choices=LETTERSTYLE, label='Letter Style')
    storeid = forms.DecimalField(required=False, label='Store ID')
    employeeid = forms.DecimalField(required=False, label='Employee ID')
    toptube = forms.CharField(required=False, label='Top Tube')
    chainstay = forms.CharField(required=False, label='Chain Stay')
    headtubeangle = forms.CharField(required=False, label='Head Tube Angle')
    seattubeangle = forms.CharField(required=False, label='Seat Tube Angle')
    listprice = forms.CharField(required=False, label='List Price')
    saleprice = forms.DecimalField(required=False, label='Sale Price')
    salestax = forms.DecimalField(required=False, label='Sales Tax')
    salestate = forms.DecimalField(required=False, label='Sale State')
    shipprice = forms.DecimalField(required=False, label='Ship Price')
    frameprice = forms.DecimalField(required=False, label='Frame Price')
    componentlist = forms.DecimalField(required=False, label='Component List')
