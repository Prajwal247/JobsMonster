from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepageview, name = 'home'),
    path('homepage', views.homeview, name = 'homepage'),
    path('base', views.testing, name = 'base'),
    path('jobcategory/<int:id>', views.jobcategory, name='jobcategory'),
    path('about/', views.about, name= "about"),
    path('developers/', views.developers, name= "developers"),
    path('contact/', views.contact, name= "contact"),


]