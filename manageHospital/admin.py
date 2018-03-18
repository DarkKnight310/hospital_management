

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(patients)
admin.site.register(patient_phone_number)
admin.site.register(department)
admin.site.register(doctors)
admin.site.register(doctor_phone_number)
admin.site.register(consults)
admin.site.register(belongs_to)
admin.site.register(receptionist)
admin.site.register(bill)
admin.site.register(maintains)
admin.site.register(appointment)
admin.site.register(login_details)
