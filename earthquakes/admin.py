from django.contrib import admin
from .models import Earthquake, Status
# Register your models here.
admin.site.register(Earthquake)
admin.site.register(Status)