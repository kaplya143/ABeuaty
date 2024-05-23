from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register(Tovar)
admin.site.register(Modal)
admin.site.register(Oplata)
admin.site.register(Profile)
admin.site.register(ServiceAppointment)