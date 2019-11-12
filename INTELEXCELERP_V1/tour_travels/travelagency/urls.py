
from django.urls import path



from .import views

urlpatterns = [
    path("", views.travelagencyadd, name="travelagencyadd"),
    path("edit/<int:pk>", views.travelagencyedit, name="travelagencyedit"),
    path("delete/<int:pk>", views.travelagencydelete, name="travelagencydelete"),
]
