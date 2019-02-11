from django.contrib import admin
from .models import hewan, kandang, penjaga, pengunjung

# Register your models here.
my_model = [hewan, kandang, penjaga, pengunjung]
admin.site.register(my_model)