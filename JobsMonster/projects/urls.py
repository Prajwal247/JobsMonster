from django.urls import path 
from . import views

urlpatterns = [
    path('initiateproject/', views.postproject, name = 'initiateproject'),
    path('project/edit/<int:id>', views.editproject, name='editproject'),
    path('project/detail/<int:id>', views.projectdetail, name='projectdetail'),
    path('project/delete/<int:id>', views.deleteproject, name='deleteproject'),
    path('enroll/<int:pid><int:uid>', views.enroll, name="enroll"),
    path('terminate/<int:uid>/<int:pid>', views.terminate, name="terminate"),
    path('sendupdates/<int:pid>', views.sendupdates, name ='sendupdates'),


]