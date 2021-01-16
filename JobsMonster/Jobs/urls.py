from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepageview, name = 'home'),
    path('base', views.testing, name = 'base'),
]