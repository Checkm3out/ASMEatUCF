
from django.urls import path
from . import views

from django.views.generic import RedirectView

app_name = "asme"
urlpatterns = [

    path('3D-Printer/', views.printer_request_form),

    path('about/', views.about),

]


from wagtail.core.models import Page
# from wagtail.core import urls as wagtail_urls

#if page models are created then Home will be the root
if Page.objects.all():
    urlpatterns += [

        path('', RedirectView.as_view(url='/asme/home/', permanent=False)),
    ]

else:
    urlpatterns += [

        path('', views.asme),
    ]