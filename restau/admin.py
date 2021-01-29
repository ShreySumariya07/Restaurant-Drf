from django.contrib import admin

# Register your models here.
from restau.models import *

admin.site.register(Restaurant)
admin.site.register(Recipe)