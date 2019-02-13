from django import forms
from .models import blog_model

class blog_modelform(forms.ModelForm): #dipake buat ke views
    class Meta:
        model = blog_model #nama kelas dari models field khusus "model"
        fields =('nama_blog', 'cerita_blog', 'foto_blog', 'comment_blog', 'tanggal_blog' )