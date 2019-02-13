from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_mentee, name = 'mentee'),
    # path('db_mentee', views.db_mentee, name = 'db_mentee'),
    path('input_mentee_model', views.input_mentee_model, name = 'input_mentee_model'),
]