from django.contrib import admin
from .models import mentor_model

# Register your models here.
my_model = [mentor_model]
admin.site.register(my_model)