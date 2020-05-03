# The views are what controls html template responses and the variables inside of them

# import here
from django.shortcuts import render, redirect
from django.conf import settings

# import the forms for the models
from .forms import EmailForm

# import the models we created
from .models import PrinterFile, OfficerModel, AboutModel

import mimetypes

import os

from django.core.mail import send_mail, EmailMessage

from wagtail.core.models import Page

# Create your views here.

# site/asme/  'home page'
def asme(request):
    args = {'name': "form", 'page1': Page.objects.all()}
    # if Page.objects.all():
    #     return redirect('/asme/home/')
    # else:
    return render(request, 'printrequest/asme.html', args)


def about(request):
    args = {'about': AboutModel.objects.all(), 'name': OfficerModel.objects.all()}
    print(args)
    return render(request, 'printrequest/about.html', args)


def printer_request_form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            print("file saved")
            print(request.FILES.get('printerfile'))
        # email = request.POST.get('email')
            subject = "Print this"
            message = ""
            for key, value in request.POST.items():
                if key == "csrfmiddlewaretoken":
                    print("--skip--")
                else:
                    message = message + key + ": " + value + "\n"
            print(message)
            #message = request.POST.dict()
            document = form.cleaned_data['document'].name
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ("wofw11@yahoo.com",)
            email = EmailMessage(subject, message, email_from, recipient_list)
            base_dir = 'media/documents/'

            email.attach_file(base_dir + str(document))

            email.send()
            print("file sent")
            os.remove(base_dir + str(document))
            print("file deleted")
            obj = PrinterFile.objects.all()
            obj.delete()
        else:
            print("form invalid")
        return redirect('/asme/home/')

    else:
        form = EmailForm()
        args = {'form': form}
        return render(request, 'printrequest/home.html', args)

