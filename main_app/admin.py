from django.contrib import admin
from .models import Patient, Provider, Record, Message

# Register your models here.

admin.site.register(Provider)
admin.site.register(Patient)
admin.site.register(Record)
admin.site.register(Message)
