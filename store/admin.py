from django.contrib import admin
from .models import *

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'state', 'city')

