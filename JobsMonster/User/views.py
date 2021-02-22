from django.shortcuts import render, reverse, redirect
from .forms import UserRegistrationForm, ProfessionalUserRegistrationForm
from django.contrib.auth import login, authenticate, logout, password_validation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from django.contrib.auth import get_user_model
from Hiring.models import Jobpost, Applicants
from projects.models import Project, ProjectManpowers

# Create your views here.
# logout function
@login_required
def Logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email, password=password)
        if user:
            if user.is_active:
                print("processing")
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(request,messages.INFO,'Account not active')
        else:
            messages.add_message(request,messages.INFO,'Invalid Login')
    return render(request, "user/login.html")


def usersignuppage(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # password_validation.validate_password(user.password)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your JobsMonster account.'
            # html_message = render_to_string('user/acc_active_email.html',{
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
            #     'token' : account_activation_token.make_token(user),
            # })
            # email = form.cleaned_data.get('email')
            # to_email = [email]
            # send_mail(mail_subject,message='Activate your account',from_email='jobsmonster247@gmail.com',recipient_list=to_email,html_message=html_message)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'user/register.html',{'form':form, })


def professionalsignuppage(request):
    if request.method == 'POST':
        form = ProfessionalUserRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # password_validation.validate_password(user.password)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your Jobsmonster account.'
            # html_message = render_to_string('user/acc_active_email.html',{
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
            #     'token' : account_activation_token.make_token(user),
            # })
            # email = form.cleaned_data.get('email')
            # to_email = [email]
            # send_mail(mail_subject,
            #           message='Activate your account',
            #           from_email='prazzwalthapa87@gmail.com',
            #           recipient_list=to_email,
            #           html_message=html_message)
            return redirect('login')
        else:
            print("helloadsfas")    
    else:
        form = ProfessionalUserRegistrationForm()
    return render(request,'user/professionalregister.html',{'form':form, })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'user/emailconfirmed.html')
    else:
        return render(request, 'user/confirmationfailed.html')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'user/emailconfirmed.html')
    else:
        return render(request, 'user/confirmationfailed.html')


def registrationchoice(request):
    return render(request, 'user/registrationchoice.html')

def userprofile(request):
    loggedin_user = User.objects.get(id=request.user.id)
    posts = Jobpost.objects.filter(posted_by=loggedin_user)
    applied_fors = Applicants.objects.filter(user_id=loggedin_user)
    hired_projects = ProjectManpowers.objects.filter(user_id=loggedin_user)
    print(hired_projects)
    projects = Project.objects.filter(initiated_by=loggedin_user)
    return render(request,'user/profile.html',{'loggedin_user':loggedin_user,'posts':posts, 'projects':projects,'hired_projects':hired_projects,'applied_fors':applied_fors})

def updateprofile(request, id):
    if request.method == 'POST':
        profileid = get_user_model().objects.get(pk = id)
        if profileid.Specialization != '':
            form = ProfessionalUserRegistrationForm(request.POST, instance = profileid)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegistrationForm(request.POST, instance = profileid)
            if form.is_valid():
                form.save()
                return redirect('login')
    else:
        profileid = get_user_model().objects.get(pk = id)
        if profileid.Specialization != '':
            form = ProfessionalUserRegistrationForm(instance=profileid)
        else:
            form = UserRegistrationForm(instance=profileid)
    return render(request, 'user/updateprofile.html', {'form':form})