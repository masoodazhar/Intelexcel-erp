from django.urls import path


from . import views


urlpatterns = [
    path("", views.employeeadd, name="employeeadd"),
    path("edit/<int:pk>", views.employeeedit, name="employeeedit"),
    path("delete/<int:pk>", views.employeedelete, name="employeedelete"),
    # path("view/<int:pk>/<str:pnr>", views.employeeview, name="employeeview"),
]
