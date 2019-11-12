from django.db import models

# Create your models here.


class TravelAgency(models.Model):

    tname = models.CharField(max_length=50, unique=True, null=True)
    contact = models.IntegerField(unique=True, null=True)
    propname = models.CharField(max_length=50, unique=True, null=True)
    procontact = models.IntegerField(unique=True, null=True)
    countername = models.CharField( max_length=50, unique=True, null=True)
    countercontact = models.IntegerField(unique=True, null=True)
    accountantname = models.CharField( max_length=50, unique=True, null=True)
    accountantcontact = models.IntegerField(unique=True, null=True)
    description = models.TextField(unique=False, null=False)

    def __str__(self):
        return self.tname

    def get_absolute_url(self):
        return reverse("TravelAgency_detail", kwargs={"pk": self.pk})
