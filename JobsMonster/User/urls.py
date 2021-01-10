from django.urls import path 
from . import views 

urlpatterns = [
    path('login/', views.loginpage, name = 'login'),
    path('usersignup/', views.usersignuppage, name = 'usersignup'),
    path('professionalsignup/', views.professionalsignuppage, name = 'professionalsignup'),


]