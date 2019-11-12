from django import forms

from .models import *

length = 50

class TravelAgencyForm(forms.ModelForm):

    tname = forms.CharField(label='Travel Agency Name', max_length=length, required=True)
    contact = forms.IntegerField(label='Travel Agency Contact', required=False)
    propname = forms.CharField(label='Propwriter Name', max_length=length, required=False)
    procontact = forms.IntegerField(label='Propwriter Contact', required=False)
    countername = forms.CharField(label='Counter Name', max_length=length, required=False)
    countercontact = forms.IntegerField(label='Counter Contact', required=False)
    accountantname = forms.CharField(label='Accountant Name', max_length=length, required=False)
    accountantcontact = forms.IntegerField(label='Accountant Contact', required=False)
    description = forms.CharField(label='Description', max_length=200, required=False, widget=forms.Textarea)


    class Meta:
        model = TravelAgency
        fields = [
            'tname',
            'contact',
            'propname',
            'procontact',
            'countername',
            'countercontact',
            'accountantname',
            'accountantcontact',
            'description'
        ]
