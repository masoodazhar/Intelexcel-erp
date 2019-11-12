




from django.urls import path, include

from django.contrib import admin


from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("accounts/", include('django.contrib.auth.urls'), name="login"),
        path('travelagency/', include('tour_travels.travelagency.urls')),
        path("customer/", include('tour_travels.customer.urls')),
        path("ticket/", include('tour_travels.tickit.urls')),
        path("employee/", include('tour_travels.employee.urls'))
]
