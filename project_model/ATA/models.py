from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class direksi(models.Model):
    Nama_Lengkap =  models.TextField(max_length = 255)
    Nomor_Telepon = models.TextField(max_length = 25)
    Jabatan = models.TextField(max_length = 100)

class Mentee(models.Model):
    Nama_Lengkap =  models.TextField(max_length = 255)
    Nomor_Telepon = models.CharField(max_length = 25)
    Nomor_absen = models.CharField(max_length = 2)
    Nilai_rerata = models.CharField(max_length = 4)    

class mata_pelajaran(models.Model):
    nama_pelajaran = models.TextField(max_length = 255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    Nama_Lengkap =  models.TextField(max_length = 255)
    Nomor_Telepon = models.CharField(max_length = 25)
    Ma_Pel = models.ForeignKey(mata_pelajaran, on_delete = models.CASCADE)

class challenge(models.Model):
    Nama_Challange =  models.TextField(max_length = 255)
    banyak_soal = models.CharField(max_length = 25)
    bobot_nilai = models.CharField(max_length = 25)
    Pelajaran = models.ForeignKey(mata_pelajaran, on_delete = models.CASCADE)

class live_code(models.Model):
    Nama_live_code =  models.TextField(max_length = 255)
    banyak_soal = models.CharField(max_length = 25)
    bobot_nilai = models.CharField(max_length = 25)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    Pelajaran = models.ForeignKey(mata_pelajaran, on_delete = models.CASCADE)