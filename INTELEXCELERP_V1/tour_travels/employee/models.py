from django.db import models
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

# class Employee(UserCreationForm):
#     usercontact = models.CharField(max_length=50)
#     usercnic = models.CharField(max_length=20)
#     isfixedsalary = models.BooleanField(choices=(('yes','yes'), ('no','no')))
#     usersalary = models.IntegerField()
    

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Employee_detail", kwargs={"pk": self.pk})
