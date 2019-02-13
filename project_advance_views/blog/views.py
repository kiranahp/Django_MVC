from django.shortcuts import render, redirect
from .models import blog_model
from .forms import blog_modelform

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {})

def db_blog(request): #dipake buat ke urls
    blog = blog_model.objects.all() #nama kelas dari model
    return render(request, "blog/blog.html", {"blogs":blog})

def input_blog_model(request): #dipake buat ke urls dan html
    if request.method == "POST":
        form = blog_modelform(request.POST) #nama kelas dari form.py
        if form.is_valid():
            form.save()
            return redirect('db_blog')
    else:
        form = blog_modelform()
    return render(request, "blog/blogform.html", {"form": form})