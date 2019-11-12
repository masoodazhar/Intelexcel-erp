from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
# Create your views here.


def employeeadd(request):
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST)
        if employeeform.is_valid():
            employeeform.save()
            messages.success(request,'employee has been saved!')
            return redirect('employeeadd')
    else:
         employeeform = EmployeeForm()

    employeedata = User.objects.all()
    context = {
        'employeeform': employeeform,
        'employeedata': employeedata
    }
    return render(request,'tour_travels/employee/index.html', context)


def employeeedit(request, pk):
    employee_data = User.objects.get(pk=pk)
    if request.method=='POST':
        employeeform = EmployeeForm(request.POST, instance=employee_data)
        if employeeform.is_valid():
            employeeform.save()
            messages.success(request,'employee has been Modified!')
            return redirect('employeeadd')
    else:
         employeeform = EmployeeForm(instance=employee_data)

    employeedata = User.objects.all()
    context = {
        'employeeform': employeeform,
        'employeedata': employeedata
    }
    return render(request,'tour_travels/employee/index.html', context)


def employeedelete(request, pk):
     employee_data = User.objects.get(pk=pk)
     employee_data.delete()
     messages.success(request,'employee has been Deleted!')
     return redirect('employeeadd')
