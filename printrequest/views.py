from django.shortcuts import render, redirect
from django.conf import settings

from .forms import EmailForm

import mimetypes

import os

from django.core.mail import send_mail, EmailMessage

# Create your views here.


def home(request):
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
                    message = message + key + ": "+ value + "\n"
            print(message)
            #message = request.POST.dict()
            document = request.FILES.get('document')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ("wofw11@yahoo.com",)
            email = EmailMessage(subject, message, email_from, recipient_list)
            base_dir = 'media/documents/'

            email.attach_file(base_dir + str(document))

            email.send()
            print("file sent")
            os.remove(base_dir + str(document))
            print("file deleted")
        else:
            print("form invalid")
        return redirect('/asme/home/')

    else:
        form = EmailForm()
        args = {'form': form}
        return render(request, 'printrequest/home.html', args)

