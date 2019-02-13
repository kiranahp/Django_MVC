from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_mentor, name = 'mentor'),
    # path('db_mentor', views.db_mentor, name = 'db_mentor'),
    path('input_mentor_model', views.input_mentor_model, name = 'input_mentor_model'),
]