
from django.urls import path
from . import views

app_name = "asme"
urlpatterns = [

    path('3D-Printer/', views.printer_request_form),
    path('', views.asme),
    path('about/', views.about),
]
