from django.db import models

# Create your models here.


# from tickit.models import Ticket

class Customer(models.Model):
    
    cname = models.CharField(max_length=50,unique=True, null=True)
    ccontact = models.IntegerField(unique=True, null=True)
    cdescription = models.TextField()

    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})

class CustomerInstallment(models.Model):
    
    customerid = models.CharField(max_length=50)
    pnr = models.CharField(max_length=50)
    paymentdate = models.DateField()
    installment = models.IntegerField()
    description = models.TextField(null=False)

    def __str__(self):
        return self.customerid

    def get_absolute_url(self):
        return reverse("CustomerInstallment_detail", kwargs={"pk": self.pk})