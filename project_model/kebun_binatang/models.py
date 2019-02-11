from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class hewan(models.Model):
    nama = models.CharField(max_length = 255)
    species =  models.TextField(max_length = 255)
    berat = models.CharField(max_length = 1)
    umur = models.TextField(max_length = 25)

class kandang(models.Model):
    nama = models.CharField(max_length = 255)
    isi_kandang =  models.TextField(max_length = 255)
    luas_kandang = models.CharField(max_length = 1)

class penjaga(models.Model):
    nama = models.TextField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    jadwal_jaga = models.DateTimeField(default=timezone.now)
    
class pengunjung(models.Model):    
    nama = models.TextField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 25)
    hari_berkunjung = models.DateTimeField(default=timezone.now)