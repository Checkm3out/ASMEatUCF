
from django.urls import path
from . import views

from django.conf.urls import url


app_name = "asme"
urlpatterns = [

    path('3D-Printer/', views.printer_request_form),
    path('', views.asme),
    path('about/', views.about),

    # path('<path>[-\w/]+)/', views.page_detail, name="page"),
    # path('', views.page_detail, name="root"),
    url(r"^(?P<path>[-\w/]+)/$", views.page_detail, name="page"),
    url(r"^$", views.page_detail, name="root"),


]
