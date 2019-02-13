from django.shortcuts import render, redirect
from .models import mentor_model
from .mentorform import mentor_modelform

# Create your views here.
def mentor(request):
    return render(request, 'mentor/mentor.html', {})

def db_mentor(request): #dipake buat ke urls
    mentor = mentor_model.objects.all() #nama kelas dari model
    return render(request, "mentor/mentor.html", {"mentors":mentor})

def input_mentor_model(request): #dipake buat ke urls dan html
    if request.method == "POST":
        form = mentor_modelform(request.POST) #nama kelas dari form.py
        if form.is_valid:
            form.save()
            return redirect('db_mentor')
    else:
        form = mentor_modelform()
    return render(request, "mentor/mentorform.html", {"form": form})