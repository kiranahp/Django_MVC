from django.contrib import admin
from .models import blog_model

# Register your models here.
my_model = [blog_model]
admin.site.register(my_model)