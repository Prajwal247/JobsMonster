from django.urls import path 
from . import views

urlpatterns = [
    path('hire/<int:id>', views.hiring, name = 'hire'),
    path('postjob/', views.postjob, name = 'postjob'),
    path('post/edit/<int:id>', views.editpost, name='editpost'),
    path('post/delete/<int:id>', views.deletepost, name='deletepost'),
    path('detail/user/<int:id>', views.detail, name='detail'),
    path('jobdetail/<int:id>', views.jobdetail, name='jobdetail'),
    path('applyjob/<int:jid>', views.applyjob, name='applyjob'),


]