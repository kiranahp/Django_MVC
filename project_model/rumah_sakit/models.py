from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class dokter(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.TextField(max_length = 25)
    bidang = models.TextField(max_length = 100)
    jadwal_praktek = models.DateTimeField(default=timezone.now)

class pasien(models.Model):
    nama = models.CharField(max_length = 50)
    nomor_telepon = models.TextField(max_length = 25)
    alamat = models.TextField(max_length = 255)
    keluhan = models.TextField(max_length = 255)

class resep(models.Model):
    nama = models.CharField(max_length = 50)
    total_harga = models.CharField(max_length = 25)
    kumpulan_obat = models.TextField(max_length = 255)

class obat(models.Model):
    nama = models.TextField(max_length = 50)
    kandungan = models.TextField(max_length = 255)
    khasiat = models.TextField(max_length = 255)