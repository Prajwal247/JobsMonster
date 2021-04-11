from django.urls import path 
from . import views

urlpatterns = [
    path('hire/<int:id>', views.hiring, name = 'hire'),
    path('postjob/', views.postjob, name = 'postjob'),
    path('post/edit/<int:id>', views.editpost, name='editpost'),
    path('post/delete/<int:id>', views.deletepost, name='deletepost'),
    path('detail/user/<int:id>', views.detail, name='detail'),
    path('biodataview/<int:id>', views.biodataview, name='biodata'),
    path('jobdetail/<int:id>', views.jobdetail, name='jobdetail'),
    path('applyjob/<int:jid>', views.applyjob, name='applyjob'),
    path('appliedjob/<int:id>', views.applyjobdetail, name='appliedjobdetail'),
    path('hiredprojectdetail/<int:id>', views.hiredprojectdetail, name='hiredprojectdetail'),
    # path('', views.declineapplication, name ='declineapplication'),
]