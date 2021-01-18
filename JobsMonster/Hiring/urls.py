from django.urls import path 
from . import views

urlpatterns = [
    path('hire/', views.hiring, name = 'hire'),
    path('postjob/', views.postjob, name = 'postjob'),
]