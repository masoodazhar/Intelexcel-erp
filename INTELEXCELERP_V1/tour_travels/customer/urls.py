
from django.urls import path



from .import views

urlpatterns = [
    path("", views.customeradd, name="customeradd"),
    path("edit/<int:pk>", views.customeredit, name="customeredit"),
    path("delete/<int:pk>", views.customerdelete, name="customerdelete"),
    path("customerinstallment/<int:getid>", views.customerinstallmentadd, name="customerinstallmentadd"),
    path("customerinstallmentedit/<int:pk>", views.customerinstallmentedit, name="customerinstallmentedit"),
    path("customerinstallmentdelete/<int:pk>", views.customerinstallmentdelete, name="customerinstallmentdelete"),
]