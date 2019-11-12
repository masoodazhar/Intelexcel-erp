from django.shortcuts import render
import numpy as np

from tour_travels.customer.models import *
from tour_travels.tickit.models import Ticket




def index(request):

    collect_remaining_amounts = []
    customerdata = Customer.objects.all()

    sum_of_all_remaining_amount = sum([doing_seperate_of_remaining['remainingamount'] for doing_seperate_of_remaining in Ticket.objects.values('remainingamount').all() ])
    sum_of_all_profit_amount = sum([doing_seperate_of_profit['profit'] for doing_seperate_of_profit in Ticket.objects.values('profit').all() ])
    sum_of_all_total_amount = sum([doing_seperate_of_totalamount['totalamount'] for doing_seperate_of_totalamount in Ticket.objects.values('totalamount').all() ])
    sum_of_all_paid_amount = sum([doing_seperate_of_paid['installment'] for doing_seperate_of_paid in CustomerInstallment.objects.values('installment').all() ])
    still_remaining_amount = sum_of_all_remaining_amount-sum_of_all_paid_amount

    nparray = Ticket.objects.values('remainingamount').all()

    print(list(nparray.values('remainingamount')))
    # print(sum_of_all_remaining_amount)
    # print(sum_of_all_profit_amount)
    # print(sum_of_all_total_amount)
    # print(sum_of_all_paid_amount)
    context = {
        'sum_of_all_remaining_amount': sum_of_all_remaining_amount,
        'sum_of_all_paid_amount': sum_of_all_paid_amount,
        'still_remaining_amount': still_remaining_amount,
        'sum_of_all_profit_amount': sum_of_all_profit_amount,

    }
    # print(get_all_remaining_amount_from_ticket)
    return render(request,'index.html',context)
