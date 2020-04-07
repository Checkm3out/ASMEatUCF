
from django.urls import path
from . import views

app_name = "asme"
urlpatterns = [

    path('home/', views.home),
    path('', views.asme),
    path('about/', views.about),
]
