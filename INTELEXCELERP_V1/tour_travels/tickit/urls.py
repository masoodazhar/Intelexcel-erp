
from django.urls import path



from .import views

urlpatterns = [
    path("", views.ticketadd, name="ticketadd"),
    path("edit/<int:pk>", views.ticketedit, name="ticketedit"),
    path("delete/<int:pk>", views.ticketdelete, name="ticketdelete"),
    path("view/<int:pk>/<str:pnr>", views.ticketview, name="ticketview"),
    path("airline", views.airlineadd, name="airlineadd"),
    path("airlineedit/<int:pk>", views.airlineedit, name="airlineedit"),
    path("airlinedelete/<int:pk>", views.airlinedelete, name="airlinedelete"),
]