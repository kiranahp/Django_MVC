from django.contrib import admin
from .models import dokter, pasien, resep, obat

# Register your models here.
my_model = [dokter, pasien, resep, obat]
admin.site.register(my_model)