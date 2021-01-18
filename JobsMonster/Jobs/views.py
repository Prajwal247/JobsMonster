from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
def homepageview(request):
    users = get_user_model().objects.all().filter(currently_employed="")
    print(users)
    
    return render(request, 'jobs/home.html',{'users':users})

def testing(request):
    return render(request, 'base.html')