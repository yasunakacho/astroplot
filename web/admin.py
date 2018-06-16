from django.contrib import admin
from .models import Cryptocurrency, Price

# Register your models here.
admin.site.register(Cryptocurrency)
admin.site.register(Price)
