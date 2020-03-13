from django.contrib import admin
from .models import Bicycle

admin.register(Bicycle)(admin.ModelAdmin)
