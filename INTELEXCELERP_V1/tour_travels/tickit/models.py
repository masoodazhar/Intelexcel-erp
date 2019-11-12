from django.db import models

# Create your models here.

from tour_travels.customer.models import Customer

class Airline(models.Model):

    aname = models.CharField(max_length=50)
    airlinecode = models.CharField(max_length=5)
    description = models.TextField()


    def __str__(self):
        return self.aname

    def get_absolute_url(self):
        return reverse("Airline_detail", kwargs={"pk": self.pk})



class Passenger(models.Model):

    pname = models.CharField(max_length=50)
    pticketno =  models.CharField(max_length=50)
    pamount = models.CharField(max_length=50)
    pcommission = models.CharField(max_length=50)
    pnrfrom = models.CharField(max_length=50)

    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        return reverse("Passenger_detail", kwargs={"pk": self.pk})



class Ticket(models.Model):

    dateofissue = models.DateField(auto_now=False, auto_now_add=False)
    root = models.CharField(max_length=50)
    traveldate = models.DateField(auto_now=False, auto_now_add=False)
    pnr = models.CharField(max_length=50)
    totalamount = models.IntegerField()
    recievedamount = models.IntegerField()
    recieveableamount = models.IntegerField()
    remainingamount = models.IntegerField()
    profit = models.IntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, default='PIA')
    madeby = models.CharField(max_length=50, default='Mubeen')
    careof = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Description = models.TextField(null=False, default=' ')

    def __str__(self):
        return self.pnr

    def get_absolute_url(self):
        return reverse("Ticket_detail", kwargs={"pk": self.pk})
