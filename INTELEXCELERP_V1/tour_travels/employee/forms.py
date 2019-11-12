from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import *


class EmployeeForm(UserCreationForm):

    usercontact = forms.CharField(max_length=50, label='User Contact')
    usercnic = forms.CharField(max_length=20, label='User CNIC')
    isfixedsalary = forms.BooleanField(
        required=False,
        label='Is Fixed Salary <br><sup>(if yes fill out the salary box) else ( fill out commission or percentage optional)</sup>',
        widget=forms.CheckboxInput(
            attrs= {
                'id': 'square-checkbox-1'
            }
        )     
     )

    usersalary = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'usercontact',
            'usercnic',
            'isfixedsalary',
            'usersalary',
            'password1',
            'password2'
        ]
