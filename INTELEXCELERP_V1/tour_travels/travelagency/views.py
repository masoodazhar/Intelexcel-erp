from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *




def travelagencyadd(request):
    if request.method=='POST':
        travelagencyform = TravelAgencyForm(request.POST)
        if travelagencyform.is_valid():
            travelagencyform.save()
            messages.success(request,'Travel Agency has been saved!')
            return redirect('travelagencyadd')
    else:
         travelagencyform = TravelAgencyForm()

    travelagencydata = TravelAgency.objects.all()
    context = {
        'travelagencyform': travelagencyform,
        'travelagencydata': travelagencydata
    }
    return render(request,'tour_travels/travelagency/index.html', context)


def travelagencyedit(request, pk):
    travelagency_data = TravelAgency.objects.get(pk=pk)
    if request.method=='POST':
        travelagencyform = TravelAgencyForm(request.POST, instance=travelagency_data)
        if travelagencyform.is_valid():
            travelagencyform.save()
            messages.success(request,'Travel Agency has been Modified!')
            return redirect('travelagencyadd')
    else:
         travelagencyform = TravelAgencyForm(instance=travelagency_data)

    travelagencydata = TravelAgency.objects.all()
    context = {
        'travelagencyform': travelagencyform,
        'travelagencydata': travelagencydata
    }
    return render(request,'tour_travels/travelagency/index.html', context)


def travelagencydelete(request, pk):
     travelagency_data = TravelAgency.objects.get(pk=pk)
     travelagency_data.delete()
     messages.success(request,'Travel Agency has been Deleted!')
     return redirect('travelagencyadd')
