from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField

# Create your models here.

class mentor_model(models.Model):
    nama_mentor = models.TextField(max_length = 50)
    profession_mentor =  models.TextField(max_length = 50)
    quotes_mentor = models.TextField()
    foto_mentor = models.ImageField(upload_to= 'mentormedia')
    
    def __str__(self):
        return self.nama_mentor
