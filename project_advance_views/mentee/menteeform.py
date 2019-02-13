from django import forms
from .models import mentee_model

class mentee_modelform(forms.ModelForm): #dipake buat ke views
    class Meta:
        mentee = mentee_model
        fields = ('nama_mentee', 'quotes_mentee', 'foto_mentee')