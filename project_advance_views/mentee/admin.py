from django.contrib import admin
from .models import mentee_model

# Register your models here.
my_model = [mentee_model]
admin.site.register(my_model)