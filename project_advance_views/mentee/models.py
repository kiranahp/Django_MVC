from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField

# Create your models here.

class mentee_model(models.Model):
    nama_mentee = models.TextField(max_length = 50)
    quotes_mentee = models.TextField()
    foto_mentee = models.ImageField(upload_to= 'menteemedia')
    
    def __str__(self):
        return self.nama_mentee