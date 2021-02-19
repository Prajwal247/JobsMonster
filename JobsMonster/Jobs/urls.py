from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepageview, name = 'home'),
    path('homepage', views.homeview, name = 'homepage'),
    path('base', views.testing, name = 'base'),
]