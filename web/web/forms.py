from django import forms

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

class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields =['modeltype', 'listprice' 'construction', 'letterstyleid',
            'framesize', 'toptube', 'chainstay', 'headtubeangle', 'seattubeangle']
