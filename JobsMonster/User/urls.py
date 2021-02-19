from django.urls import path 
from . import views 

urlpatterns = [
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.Logoutview, name = 'logout'),
    path('usersignup/', views.usersignuppage, name = 'usersignup'),
    path('professionalsignup/', views.professionalsignuppage, name = 'professionalsignup'),
    path('activate/<uidb64>/<token>/',views.activate,name='activate'),
    path('userchoice/', views.registrationchoice, name = 'choice'),
    path('userprofile/', views.userprofile, name = 'userprofile'),
    path('userprofile/update/<int:id>', views.updateprofile, name='updateprofile'),



]