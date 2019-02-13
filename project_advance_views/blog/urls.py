from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_blog, name = 'blog'),
    # path('db_blog', views.db_blog, name = 'db_blog'),
    path('input_blog_model/', views.input_blog_model, name = 'input_blog_model'),
]