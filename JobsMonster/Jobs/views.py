from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from Hiring.models import Jobpost
# Create your views here.
def homepageview(request):
    jobs = Jobpost.objects.all()
    users  = get_user_model().objects.exclude(Specialization='')
    current_user = request.user
    context = {'user':current_user, 'users':users,'jobs':jobs}
    if not current_user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'jobs/home.html',context)

def testing(request):
    return render(request, 'base.html')