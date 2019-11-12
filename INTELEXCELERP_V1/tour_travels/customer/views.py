from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
from tour_travels.tickit.models import Ticket
# Create your views here.



def customeradd(request):
    if request.method=='POST':
        customerform = CustomerForm(request.POST)
        if customerform.is_valid():
            customerform.save()
            messages.success(request,'Customer has been saved!')
            if(request.POST.get('ajax')):
                select_last_customer_object = Customer.objects.all().last()
                return JsonResponse({'name': select_last_customer_object.cname, 'pk': select_last_customer_object.id})
            else:
                return redirect('customeradd')
    else:
         customerform = CustomerForm()

    collect_remaining_amount_array_with_name = []
    collect_remaining_amints = []
    getting_all_installment_after_paid_from_customer=[]
    customerdata = Customer.objects.all()
    print('========================================')
    for customer in customerdata:
        collect_remaining_amints.clear()
        getting_all_installment_after_paid_from_customer.clear()
        remaining_amount_of_careof = Ticket.objects.values('remainingamount').filter(careof=customer)

        for customerinstallmentddd in CustomerInstallment.objects.values('installment').filter(customerid=customer.cname):
            getting_all_installment_after_paid_from_customer.append(customerinstallmentddd['installment'])

        for s in remaining_amount_of_careof:
            collect_remaining_amints.append(s['remainingamount'])

        collect_remaining_amount_array_with_name.append({'pk': customer.pk, 'cname': customer.cname,'remainingamountwas':sum(collect_remaining_amints), 'stillremaining': sum(collect_remaining_amints)-sum(getting_all_installment_after_paid_from_customer),'installmentPaid':sum(getting_all_installment_after_paid_from_customer), 'ccontact': customer.ccontact})

            # print(customerinstallmentddd)

    print(collect_remaining_amount_array_with_name)
        # for remaining_amount in remaining_amount_of_careof:
        #     collect_remaining_amount_array.append({'customer': remaining_amount.careof, 'sum': remaining_amount.remainingamount})
            #print(remaining_amount)


    context = {
        'customerform': customerform,
        'customerdata': collect_remaining_amount_array_with_name
    }
    if(request.POST.get('ajax')):
        return HttpResponse('error')
    else:
        return render(request,'tour_travels/customer/index.html', context)


def customeredit(request, pk):
    customer_data = Customer.objects.get(pk=pk)
    if request.method=='POST':
        customerform = CustomerForm(request.POST, instance=customer_data)
        if customerform.is_valid():
            customerform.save()
            messages.success(request,'Customer has been Modified!')
            return redirect('customeradd')
    else:
         customerform = CustomerForm(instance=customer_data)

    customerdata = Customer.objects.all()
    context = {
        'customerform': customerform,
        'customerdata': customerdata
    }
    return render(request,'tour_travels/customer/index.html', context)


def customerdelete(request, pk):
     customer_data = Customer.objects.get(pk=pk)
     customer_data.delete()
     messages.success(request,'Customer has been Deleted!')
     return redirect('customeradd')


customer_id = 0


def customerinstallmentadd(request,getid):
    customer_id = getid
    if request.method=='POST':
        geting_cutomer_name = Customer.objects.values('cname').get(pk=getid)
        getting_all_pnr_sold_to_this_customer = Ticket.objects.values('id','pnr').filter(careof=getid)
        collect_remaining_amints =[]
        getting_all_installment_after_paid_from_customer=[]
        remaining_amount_of_careof = Ticket.objects.values('remainingamount').filter(careof=getid)
        for s in remaining_amount_of_careof:
            collect_remaining_amints.append(s['remainingamount'])

        # customerinstallmentform = CustomerInstallmentForm(initial={'customerid':geting_cutomer_name['cname']})
        customerinstallmentform = CustomerInstallmentForm(request.POST)
        if customerinstallmentform.is_valid():
            customerinstallmentform.save()
            messages.success(request,'customerinstallment has been saved!')
            return redirect('customerinstallmentadd',getid=getid)
    else:
        #  customerinstallmentform = CustomerInstallmentForm(customerid='ss',pnr='fffff', paymentdate='10-10-2019', installmentamount=100)
        # customerinstallmentform = CustomerInstallmentForm()
        geting_cutomer_name = Customer.objects.values('cname').get(pk=getid)
        getting_all_pnr_sold_to_this_customer = Ticket.objects.values('id','pnr','remainingamount').filter(careof=getid)
        collect_remaining_amints =[]
        getting_all_installment_after_paid_from_customer=[]

        remaining_amount_of_careof = Ticket.objects.values('remainingamount').filter(careof=getid)
        for s in remaining_amount_of_careof:
            collect_remaining_amints.append(s['remainingamount'])

        for customerinstallmentddd in CustomerInstallment.objects.values('installment').filter(customerid=geting_cutomer_name['cname']):
            getting_all_installment_after_paid_from_customer.append(customerinstallmentddd['installment'])

        customerinstallmentform = CustomerInstallmentForm(initial={'customerid':geting_cutomer_name['cname']})

        # amount_per_pnr_on_specific_customer =
    print('================gfdgfdgfdgfdgfdgfdgfdg================')
    print(getting_all_installment_after_paid_from_customer)
        # print()

    customername = Customer.objects.values('cname').get(pk=getid)
    customerinstallmentdata = CustomerInstallment.objects.all()
    still_remaining_amount_from_customer = sum(collect_remaining_amints)-sum(getting_all_installment_after_paid_from_customer)
    # print(customerinstallmentdata)

    context = {
        'customerinstallmentform': customerinstallmentform,
        'customerinstallmentdata': customerinstallmentdata,
        'all_pnr_this_customer': getting_all_pnr_sold_to_this_customer,
        'customername': customername['cname'],
        'collect_remaining_amints': sum(collect_remaining_amints),
        'number_of_columns': getting_all_pnr_sold_to_this_customer.count(),
        'getting_all_installment_after_paid_from_customer': sum(getting_all_installment_after_paid_from_customer),
        'still_remaining_amount_from_customer': still_remaining_amount_from_customer
    }
    return render(request,'tour_travels/customer/customerinstallment.html', context)


def customerinstallmentedit(request, pk):
    customerinstallment_data = CustomerInstallment.objects.get(pk=pk)
    if request.method=='POST':
        customerinstallmentform = CustomerInstallmentForm(request.POST, instance=customerinstallment_data)
        if customerinstallmentform.is_valid():
            customerinstallmentform.save()
            messages.success(request,'customerinstallment has been Modified!')
            return redirect('customerinstallmentadd',getid=customer_id)
    else:
         customerinstallmentform = CustomerInstallmentForm(instance=customerinstallment_data)

    customerinstallmentdata = CustomerInstallment.objects.all()
    context = {
        'customerinstallmentform': customerinstallmentform,
        'customerinstallmentdata': customerinstallmentdata
    }
    return render(request,'tour_travels/customer/customerinstallment.html', context)


def customerinstallmentdelete(request, pk):
     customerinstallment_data = CustomerInstallment.objects.get(pk=pk)
     customerinstallment_data.delete()
     messages.success(request,'customerinstallment has been Deleted!')
     return redirect('customerinstallmentadd',getid=customer_id)
