from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone
from django.db.models import ImageField

# Create your models here.

class blog_model(models.Model):
    nama_blog = models.TextField(max_length = 50)
    cerita_blog = models.TextField()
    foto_blog = models.ImageField(upload_to= 'blogmedia')
    tanggal_blog = models.DateTimeField(default=timezone.now)
    comment_blog = models.TextField()
    
    def __str__(self):
        return self.nama_blog