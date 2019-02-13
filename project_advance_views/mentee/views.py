from django.shortcuts import render, redirect
from .models import mentee_model
from .menteeform import mentee_modelform

# Create your views here.
def mentee(request):
    return render(request, 'mentee/mentee.html', {})

def db_mentee(request): #dipake buat ke urls
    mentee = mentee_model.objects.all() #nama kelas dari model
    return render(request, "mentee/mentee.html", {"mentees":mentee})

def input_mentee_model(request): #dipake buat ke urls dan html
    if request.method == "POST":
        form = mentee_modelform(request.POST) #nama kelas dari form.py
        if form.is_valid:
            form.save()
            return redirect('db_mentee')
    else:
        form = mentee_modelform()
    return render(request, "mentee/menteeform.html", {"form": form})