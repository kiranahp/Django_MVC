from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class Mentee(models.Model):
    name = models.CharField(max_length = 255)
    full_name =  models.TextField(max_length = 255)
    gender = models.CharField(max_length = 1)
    telephone = models.TextField(max_length = 25)
    mobile = models.TextField(max_length = 25)
    adress = models.TextField(max_length = 255)
    nick_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class post(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    title = models.TextField(max_length = 255)
    content = models.TextField(max_length = 255)
    created_by = models.TextField(max_length = 255)
    posted_by = models.ForeignKey(Mentee, on_delete = models.CASCADE)