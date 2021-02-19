from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Jobpost
from django.contrib.auth import get_user_model
from . import forms
# Create your views here.

def hiring(request, id):
    form = forms.HiringForm()
    if request.method == 'POST':
        form = forms.HiringForm(request.POST)
        sender=request.user
        if form.is_valid():
            adress=form.cleaned_data['address']
            date=form.cleaned_data['date']
            required_for=form.cleaned_data['Required_for']
            estimated_time=form.cleaned_data['estimated_duration']
            description=form.cleaned_data['description']

            subject="%s wants to hire you"%(sender)
            message="%s wants to hire you for %s for the estimated time of %s hrs on %s\n Description: %s"%(sender,required_for,estimated_time,date,description)
            user=get_user_model().objects.get(pk=id)
            send_mail(
            subject=subject,
            message=message,
            from_email='prazzwalthapa87@gmail.com',
            recipient_list=[user],
            fail_silently=False,
        )
            form.save()
            return redirect('home')
    return render(request, 'hiring/hiringform.html',{'form':form})

def postjob(request):
    form = forms.PostJobForm()
    if request.method == 'POST':
        form = forms.PostJobForm(request.POST)
        form.instance.posted_by = request.user
        if form.is_valid():
            category=form.cleaned_data['category']
            description=form.cleaned_data.get('description')
            date=form.cleaned_data.get('date')
            
            estimatedtime=form.cleaned_data.get('estimated_time')
            user=request.user
            subject="A job of your category is available please check your profile"
            message="a job of your category %s is posted by %s \n %s \nDate:%s time:%s" %(category,user,description,date,estimatedtime)
            send_mail(
            subject=subject,
            message=message,
            from_email='prazzwalthapa87@gmail.com',
            recipient_list=['prazzwalthapa87@gmail.com'],
            fail_silently=False,
        )
            form.save()
            return redirect('home')
    return render(request, 'hiring/postjob.html', {'form':form})

def editpost(request, id):
    if request.method == 'POST':
        postid = Jobpost.objects.get(pk = id)
        form = forms.PostJobForm(request.POST, instance = postid)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        postid = Jobpost.objects.get(pk = id)
        form = forms.PostJobForm(instance = postid)
    return render(request, 'hiring/postedit.html', {'form':form})

def deletepost(request, id):
    post=Jobpost.objects.get(pk=id)
    post.delete()
    return redirect('userprofile')


def detail(request, id):
    user = get_user_model().objects.get(pk=id)
    return render(request, 'hiring/freelancerdetail.html',{'user':user})

def jobdetail(request, id):
    job = Jobpost.objects.get(pk=id)
    return render(request, 'hiring/postdetail.html', {'job':job})