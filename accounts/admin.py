from django.contrib import admin

from .models import CustomUser, Trainer

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Trainer)
