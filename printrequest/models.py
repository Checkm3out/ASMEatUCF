from django.db import models


class PrinterFile(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=100, default='')
    email = models.EmailField()
    member = models.CharField(max_length=1000, default='')
    model_name = models.CharField(max_length=1000, default='')
    creator = models.CharField(max_length=1000, default='')
    dimensions = models.CharField(max_length=1000, default='')
    color = models.CharField(max_length=1000, default='')
    special_requests = models.CharField(max_length=1000, default='')
    message = models.CharField(max_length=20000, default='')
    document = models.FileField(upload_to='documents/')


