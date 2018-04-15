from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PatientInfo)
admin.site.register(CheckIn)
admin.site.register(VisitInfo)
admin.site.register(EyeCare)
