from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
from tour_travels.customer.forms import CustomerForm
# Create your views here.


def ticketadd(request):
    values_of_ticket_and_passenger = []
    if request.method=='POST':

        # ticketform = TicketForm(request.POST)
        # careof = null
        if request.POST.get('careof')=='':
            careof = Customer()
        else:
            careof = Customer.objects.get(pk=request.POST.get('careof'))
        ticketformd = Ticket(
            dateofissue=request.POST.get('dateofissue'),
            root = request.POST.get('root'),
            traveldate = request.POST.get('traveldate'),
            pnr = request.POST.get('pnr'),
            totalamount = request.POST.get('totalamount'),
            recievedamount = request.POST.get('recievedamount'),
            recieveableamount = request.POST.get('recieveableamount'),
            remainingamount = request.POST.get('remainingamount'),
            profit = request.POST.get('profit'),
            airline = Airline.objects.get(pk=request.POST.get('airline')),
            madeby = request.POST.get('madeby'),
            careof =careof,
            Description = request.POST.get('Description')
        )
        # GETTING PNR ON GLOBAL VARIABLE FOR PASSING INTO PASSENGER
        pnr = request.POST.get('pnr');
        ticketform = TicketForm(request.POST)

        # passing passenger data in Passenger CLASS
        passengerformd = Passenger(
            pname=request.POST.get('pname'),
            pticketno=request.POST.get('pticketno'),
            pamount=request.POST.get('pamount'),
            pcommission=request.POST.get('pcommission'),
            pnrfrom=request.POST.get('pnr')
        )

        # GETTING RANGE JQUERY GENERATED ROWS COUNT FOR TEXTBOXES
        if request.POST.get('range'):
            number_of_rows_was_entered_from_jquery=request.POST.get('range')
        else:
            number_of_rows_was_entered_from_jquery=0

        passengerform = PassengerForm(request.POST)

        passengerformsave = request.POST
        if passengerformsave.get('range'):
            ranges =  int(passengerformsave.get('range'))
        else:
            ranges = 0;

        for cols in range(0,ranges+1):
            pnames = ''
            pticketno = ''
            pticketamount = ''
            pcommissionamount = ''
            if cols <1:
                pticketno = 'pticketno'
                pnames = 'pname'
                pticketamount = 'pamount'
                pcommissionamount = 'pcommission'
                pasname = passengerformsave.get(pnames)
                passtno = passengerformsave.get(pticketno)
                passamount = passengerformsave.get(pticketamount)
                passcommssion = passengerformsave.get(pcommissionamount)
                values_of_ticket_and_passenger.append({'pticketno':passtno, 'pticketamount':passamount,'pname':pasname,'pcommission': passcommssion })
            else:
                pticketno = f'pticketno{cols}'
                pticketamount = f'pamount{cols}'
                pcommissionamount = f'pcommission{cols}'
                pnames = f'pname{cols}'
                pasname = passengerformsave.get(pnames)
                passtno = passengerformsave.get(pticketno)
                passamount = passengerformsave.get(pticketamount)
                passcommssion = passengerformsave.get(pcommissionamount)
                values_of_ticket_and_passenger.append({'pticketno':passtno, 'pticketamount':passamount,'pname':pasname,'pcommission': passcommssion })
        print('=======================')
        print(values_of_ticket_and_passenger)
        print('=======================')
        if ticketform.is_valid():
            ticketformd.save()
            # saving all passengers on same PNR generated by jquery text boxes
            for passengers in values_of_ticket_and_passenger:
                # print(passengers['pname'])
                passengerdata_to_save = Passenger(pname=passengers['pname'], pticketno=passengers['pticketno'], pamount=passengers['pticketamount'],pcommission=passengers['pcommission'],pnrfrom=pnr)
                passengerdata_to_save.save()

            # print(values_of_ticket_and_passenger)
            messages.success(request,'ticket has been saved!')
            return redirect('ticketadd')
    else:
         ticketform = TicketForm()
         number_of_rows_was_entered_from_jquery=0

         passengerform = PassengerForm()
    # print(values_of_ticket_and_passenger)
    ticketdata = Ticket.objects.all()
    passengerdatacount = Passenger.objects.all().count()

    explodedata = []
    for i in ticketdata:
        explodedata.append(
        {
         'pk':i.pk,
         'totalamount': i.totalamount,
         'recievedamount': i.recievedamount,
         'remainingamount': i.remainingamount ,
         'customer': i.careof ,
         'pnr': i.pnr,
         'PROFIT': i.profit,
         'passnger': Passenger.objects.values('pnrfrom').filter(pnrfrom=i.pnr).count()
         })

    airlineform = AirlineForm()
    customerform = CustomerForm()
    print(explodedata)
    context = {
        'ticketform': ticketform,
        'ticketdata': explodedata,
        'passengerform': passengerform,
        'passengerdatacount': passengerdatacount,
        'number_of_rows_was_entered_from_jquery': range(0,int(number_of_rows_was_entered_from_jquery)),
        'values_of_ticket_and_passenger': values_of_ticket_and_passenger,
        'airlineform': airlineform,
        'customerform': customerform
    }
    return render(request,'tour_travels/ticket/index.html', context)


def ticketedit(request, pk):
    ticket_data = Ticket.objects.get(pk=pk)
    if request.method=='POST':
        ticketform = TicketForm(request.POST, instance=ticket_data)
        if ticketform.is_valid():
            ticketform.save()
            messages.success(request,'ticket has been Modified!')
            return redirect('ticketadd')
    else:
         ticketform = TicketForm(instance=ticket_data)

    ticketdata = Ticket.objects.all()
    context = {
        'ticketform': ticketform,
        'ticketdata': ticketdata
    }
    return render(request,'tour_travels/ticket/index.html', context)



def ticketdelete(request, pk):
     ticket_data = Ticket.objects.get(pk=pk)
     ticket_data.delete()
     messages.success(request,'ticket has been Deleted!')
     return redirect('ticketadd')


def ticketview(request, pk, pnr):
    ticketdata = Ticket.objects.filter(pk=pk).first()
    passengerdata = Passenger.objects.filter(pnrfrom=pnr)
    context = {
        'ticketdata': ticketdata,
        'passengerdata': passengerdata
    }
    return render(request,'tour_travels/ticket/view.html', context)


def airlineadd(request):
    if request.method=='POST':
        airlineform = AirlineForm(request.POST)
        if airlineform.is_valid():
            airlineform.save()
            messages.success(request,'airline has been saved!')
            if request.POST.get('ajax'):
                select_last_airline_object = Airline.objects.all().last()
                return JsonResponse({'name':select_last_airline_object.aname, 'pk': select_last_airline_object.id})
            else:
                return redirect('airlineadd')

    else:
         airlineform = AirlineForm()

    airlinedata = Airline.objects.all()
    name_and_id = Airline.objects.all().last()
    print(name_and_id)
    context = {
        'airlineform': airlineform,
        'airlinedata': airlinedata
    }
    if request.POST.get('ajax'):
        return HttpResponse('error')
    else:
        return render(request,'tour_travels/airline/airline.html', context)
    # return HttpResponse('error')


def airlineedit(request, pk):
    airline_data = Airline.objects.get(pk=pk)
    if request.method=='POST':
        airlineform = AirlineForm(request.POST, instance=airline_data)
        if airlineform.is_valid():
            airlineform.save()
            messages.success(request,'airline has been Modified!')
            return redirect('airlineadd')
    else:
         airlineform = AirlineForm(instance=airline_data)

    airlinedata = Airline.objects.all()
    context = {
        'airlineform': airlineform,
        'airlinedata': airlinedata
    }
    return render(request,'tour_travels/ticket/airline.html', context)


def airlinedelete(request, pk):
     airline_data = Airline.objects.get(pk=pk)
     airline_data.delete()
     messages.success(request,'airline has been Deleted!')
     return redirect('airlineadd')
