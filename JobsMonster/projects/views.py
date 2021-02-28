from django.shortcuts import render,redirect
from .forms import ProjectForm, UpdateForm
from .models import Project, ProjectManpowers
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


# Create your views here.

def postproject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form.instance.initiated_by = request.user
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    return render(request, 'projects/postprojects.html', {'form':form})

def editproject(request, id):
    if request.method == 'POST':
        projectid = Project.objects.get(pk = id)
        form = ProjectForm(request.POST, instance = projectid)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        projectid = Project.objects.get(pk = id)
        form = ProjectForm(instance = projectid)
    return render(request, 'projects/editproject.html', {'form':form})

def projectdetail(request, id):
    users  = get_user_model().objects.exclude(Specialization='')
    project = get_object_or_404(Project, pk=id)
    users=users.order_by('?')
    manpowers=ProjectManpowers.objects.filter(project_id=project)
    # paginator for manpower
    paginator_manpower = Paginator(manpowers,4)
    page_number_manpower = request.GET.get('page')
    page_obj_manpowers = paginator_manpower.get_page(page_number_manpower)

    # paginator for suggestions
    paginator_users = Paginator(users, 3)
    page_number_users = request.GET.get('page')
    page_obj_users = paginator_users.get_page(page_number_users)

    return render(request, 'projects/projectdetail.html', {'project':project,'page_obj_users':page_obj_users,'page_obj_manpowers':page_obj_manpowers})

def deleteproject(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect('userprofile')


def enroll(request, pid, uid):
    manpower = get_user_model().objects.get(pk=uid)
    project = get_object_or_404(Project, pk=pid)
    mp= ProjectManpowers.objects.filter(user_id=manpower, project_id=project)
    if not mp:
        u = get_user_model().objects.get(pk=uid)
        u.total_hiring+=1
        u.save()
        mp= ProjectManpowers(user_id=manpower, project_id=project)
        mp.save()
    else:
        messages.add_message(request, messages.INFO, 'User alrady in the project')
    users  = get_user_model().objects.exclude(Specialization='')
    users=users.order_by('?')
    manpowers=ProjectManpowers.objects.filter(project_id=project)
    # paginator for manpower
    paginator_manpower = Paginator(manpowers,4)
    page_number_manpower = request.GET.get('page')
    page_obj_manpowers = paginator_manpower.get_page(page_number_manpower)

    # paginator for suggestions
    paginator_users = Paginator(users, 3)
    page_number_users = request.GET.get('page')
    page_obj_users = paginator_users.get_page(page_number_users)

    return render(request, 'projects/projectdetail.html', {'project':project,'page_obj_users':page_obj_users,'page_obj_manpowers':page_obj_manpowers})
 

def terminate(request, uid, pid):
    project = Project.objects.get(pk=pid)
    send_mail(
            subject="About the termination",
            message="Sorry to say but you are terminated from the Projec: %s"%(project),
            from_email='prazzwalthapa87@gmail.com',
            recipient_list=[uid],
            fail_silently=True,
        )
    mp = ProjectManpowers.objects.get(user_id=uid, project_id=pid)
    mp.delete()
    users  = get_user_model().objects.exclude(Specialization='')
    users=users.order_by('?')
    manpowers=ProjectManpowers.objects.filter(project_id=project)
     # paginator for manpower
    paginator_manpower = Paginator(manpowers,4)
    page_number_manpower = request.GET.get('page')
    page_obj_manpowers = paginator_manpower.get_page(page_number_manpower)

    # paginator for suggestions
    paginator_users = Paginator(users, 3)
    page_number_users = request.GET.get('page')
    page_obj_users = paginator_users.get_page(page_number_users)

    return render(request, 'projects/projectdetail.html', {'project':project,'page_obj_users':page_obj_users,'page_obj_manpowers':page_obj_manpowers})
 



def sendupdates(request, pid):
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        sender=request.user
        if form.is_valid():
            subject=form.cleaned_data['subject']
            description=form.cleaned_data['description']
            users=ProjectManpowers.objects.filter(project_id=pid)
            user = []
            for u in users:
                user.append(u.user_id.email)  
            for u in user:
                send_mail(
                subject=subject,
                message=description,
                from_email=sender,
                recipient_list=[u],
                fail_silently=True,
                 )
            form.save()
            users  = get_user_model().objects.exclude(Specialization='')
            project = Project.objects.get(pk=pid)
            users=users.order_by('?')
            manpowers=ProjectManpowers.objects.filter(project_id=project)
             # paginator for manpower
            paginator_manpower = Paginator(manpowers,4)
            page_number_manpower = request.GET.get('page')
            page_obj_manpowers = paginator_manpower.get_page(page_number_manpower)

            # paginator for suggestions
            paginator_users = Paginator(users, 3)
            page_number_users = request.GET.get('page')
            page_obj_users = paginator_users.get_page(page_number_users)

            return render(request, 'projects/projectdetail.html', {'project':project,'page_obj_users':page_obj_users,'page_obj_manpowers':page_obj_manpowers})
 
    return render(request, 'projects/updateform.html',{'form':form})