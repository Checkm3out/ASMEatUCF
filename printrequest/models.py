from django.db import models
from phone_field import PhoneField


class Colors(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    price = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return (self.name + " " + self.price)

#
# class RoleModel(models.Model):
#     name = models.CharField(max_length=30, default='', blank=True)
#
#     def __str__(self):
#         return self.name


class PrinterFile(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = PhoneField(blank=True, default='')
    email = models.EmailField()
    member = models.CharField(max_length=1000, default='')
    model_name = models.CharField(max_length=1000, default='')
    creator = models.CharField(max_length=1000, default='')
    dimensions = models.CharField(max_length=1000, default='')
    color = models.ForeignKey(Colors, on_delete=models.SET_NULL, null=True)
    special_requests = models.CharField(max_length=1000, default='')
    message = models.CharField(max_length=20000, default='')
    document = models.FileField(upload_to='documents/')

#
# class OfficerModel(models.Model):
#     name = models.CharField(max_length=100, default='')
#     #role = models.ForeignKey(RoleModel, on_delete=models.SET_NULL, null=True)
#     description = models.CharField(max_length=1000, default='')



