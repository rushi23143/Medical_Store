from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StoreType)
admin.site.register(MedicalStore)
admin.site.register(MedicineType)
admin.site.register(MedicineDetails)
