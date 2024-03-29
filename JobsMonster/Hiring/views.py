from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Jobpost, Applicants
from projects.models import Project, ProjectManpowers
from django.contrib.auth import get_user_model
from . import forms
from datetime import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

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
            user.total_hiring+=1
            user.save()
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

def biodataview(request, id):
    fs = FileSystemStorage()
    file = get_user_model().objects.get(pk=id)
    filename = str(file.BioData)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment/filename="mypdf"'

            return response
    else:
        return HttpResponseNotFound("no such file exists in the database")

def jobdetail(request, id):
    job = Jobpost.objects.get(pk=id)
    applicants = Applicants.objects.filter(jobpost_id=job)
    return render(request, 'hiring/postdetail.html', {'job':job, 'applicants':applicants})

def applyjob(request, jid):
    user = request.user
    job = Jobpost.objects.get(pk=jid)
    post = Applicants.objects.filter(jobpost_id=job,user_id=user)
    if not post:
        post = Applicants(user_id=user, jobpost_id=job, applied_date=datetime.now())
        post.save()
    else:
        messages.add_message(request, messages.INFO, 'Already applied for this Job')
        return redirect('home')
    return redirect('userprofile')

# def declineapplication(request, uid, jid):
#     user = get_user_model().objects.get(pk=uid)
#     post = Jobpost.objects.get(pk=jid)
#     send_mail(
#             subject="About the application declined",
#             message="your application to the post %s have been Rejectd thank you for applying"%(post),
#             from_email='prazzwalthapa87@gmail.com',
#             recipient_list=[user],
#             fail_silently=True,
#         )
#     postt = Applicants.objects.get(user_id=uid, jobpost_id=pid)
#     postt.delete()
#     applicants = Applicants.objects.filter(jobpost_id=pid)
#     return redirect('home')
    
def applyjobdetail(request, id):
    job = Jobpost.objects.get(pk=id)
    applicants = Applicants.objects.filter(jobpost_id=job)
    print(applicants)
    length = len(applicants)
    return render(request, 'appliedjob.html',{'job':job, 'length':length,})

def hiredprojectdetail(request, id):
    project = Project.objects.get(pk=id)
    breakpoint()
    manpowers = ProjectManpowers.objects.filter(project_id=project)
    length = len(manpowers)
    return render(request, 'hiredprojectdetail.html', {'project':project, 'length':length,})