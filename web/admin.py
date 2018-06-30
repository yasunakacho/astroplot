from django.contrib import admin
from .models import Cryptocurrency, Price, Alert

# Register your models here.
admin.site.register(Cryptocurrency)
admin.site.register(Price)
admin.site.register(Alert)
