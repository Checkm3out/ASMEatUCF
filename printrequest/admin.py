from django.contrib import admin

from .models import PrinterFile, OfficerModel, OfficerTitleModel, AboutModel

admin.site.register(PrinterFile)
# admin.site.register(Colors)
admin.site.register(OfficerModel)
admin.site.register(OfficerTitleModel)
admin.site.register(AboutModel)
