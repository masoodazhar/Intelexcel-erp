from django import forms

from .models import *
from tour_travels.tickit.models import Ticket
length = 50



class CustomerInstallmentForm(forms.ModelForm):

    # pnr = forms.ChoiceField(choices= [(i.id, i.pnr) for i in Ticket.objects.defer('id','pnr')])
    paymentdate = forms.CharField(
        max_length=length,
        required=True,
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    customerid = forms.CharField(
        max_length=length,
        required=False,
        label='Customer Name',
        widget=forms.TextInput
    )
    installment = forms.CharField(
        max_length=length,
        required=True,
        label='Installment Amount',
        widget=forms.TextInput(
            attrs={
                'type': 'number'
            }
        )
    )
    pnr = forms.CharField(
        max_length=length,
        required=True,
        label='PNR',
        widget=forms.Select
    )

    description = forms.CharField(
        max_length=200,
        required=False,
        label='Description',
        widget=forms.Textarea
    )

    class Meta:
        model = CustomerInstallment
        fields = [
            'customerid',
            'pnr',
            'paymentdate',
            'installment',
            'description'

        ]


class CustomerForm(forms.ModelForm):

    cname = forms.CharField(label='Coustomer Name', max_length=length, required=True)
    ccontact = forms.IntegerField(label='Customer Contact', required=True)

    cdescription = forms.CharField(
    label = 'Description',
    max_length=200,
    required=False,
    widget=forms.Textarea(
            attrs = {
                'rows': 2
            }
        )
    )
    class Meta:
        model = Customer
        fields = [
            'cname',
            'ccontact',
            'cdescription'
        ]
