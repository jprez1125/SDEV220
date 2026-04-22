from django.contrib import admin
from .models import User, Pet, ServiceType, Appointment, Reminder

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(ServiceType)
admin.site.register(Appointment)
admin.site.register(Reminder)