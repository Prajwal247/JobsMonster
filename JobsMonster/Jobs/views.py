from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from Hiring.models import Jobpost
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def homepageview(request):
    jobs = Jobpost.objects.all().order_by('id')
    users  = get_user_model().objects.exclude(Specialization='').order_by('?')
    print(users)
    current_user = request.user
    # Paginator for jobspost
    paginator_jobs = Paginator(jobs,4)
    page_number_jobs = request.GET.get('page')
    page_obj_jobs = paginator_jobs.get_page(page_number_jobs)
    # paginator for users
    paginator_user = Paginator(users,4)
    page_number_user = request.GET.get('page')
    page_obj_user = paginator_user.get_page(page_number_user)

    context = {'user':current_user, 'users':users,'jobs':jobs,'page_obj_user':page_obj_user,'page_obj_jobs':page_obj_jobs}
    if not current_user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, 'jobs/home.html',context)
    
def homeview(request):
    return render(request,'jobs/homepage.html')

def testing(request):
    return render(request, 'base.html')

def jobcategory(request, id):
    user = get_user_model().objects.get(pk=id)
    categori = user.Specialization
    jobs = Jobpost.objects.filter(category = categori)
    print(jobs)
    return render(request, 'jobs/jobscategory.html', {'jobs':jobs})

# category functions


def about(request):
    return render(request, 'about.html')
    


def developers(request):
    return render(request, 'developers.html')


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
          subject=subject,
          message=message,
          from_email=email,
          recipient_list=['jobsmonster247@gmail.com'],
          fail_silently=False,
        )
        messages.add_message(request, messages.INFO, 'Your queries has been submitted we will get back to you soon')
        
    return render(request, 'contact.html')