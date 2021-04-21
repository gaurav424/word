from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Record)
admin.site.register(Survey)
admin.site.register(Organization)