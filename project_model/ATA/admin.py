from django.contrib import admin
from .models import direksi, Mentee, mata_pelajaran, Mentor, challenge, live_code

# Register your models here.
my_model = [direksi, Mentee, mata_pelajaran, Mentor, challenge, live_code]
admin.site.register(my_model)