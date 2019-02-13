from django import forms
from .models import mentor_model

class mentor_modelform(forms.ModelForm): #dipake buat ke views
    class Meta:
        mentor = mentor_model
        fields = ('nama_mentor', 'profession_mentor', 'quotes_mentor', 'foto_mentor')