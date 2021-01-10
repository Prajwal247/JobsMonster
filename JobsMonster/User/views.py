from django.shortcuts import render, reverse
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

# Create your views here.
def loginpage(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user:

            if user.is_active:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.add_message(request, messages.INFO, 'Account not active')
        else:
            messages.add_message(request, messages.INFO, 'Invalid login')
    

    return render(request, 'user/login.html')


def usersignuppage(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # password_validation.validate_password(user.password)
            user.active = False
            user.save()
            current_site = get_current_site(request)

            mail_subject = "activate your JobsMonster Account"
            html_message = render_to_string('user/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token':account_activation_token.make_token(user),

            })

            email = form.cleaned_data.get('email')
            to_email = [email]
            send_mail(mail_subject, message = 'Activate your account', from_email = 'prazzwalthapa87@gmail.com', recipient_list = to_email, html_message = html_message)

            return render(request, 'user/confirmemail.html')
        else:
            print("user is not valid")
            form = UserRegistrationForm()
    return render(request, 'user/register.html',{'form':form})


def professionalsignuppage(request):
    form = ProfessionalUserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return render(request, 'user/login.html')
        else:
            print("user is not valid")
            form = ProfessionalUserRegistrationForm()
    return render(request, 'user/professionalregister.html',{'form':form})

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
        return render(request, 'registration/emailconfirmed.html')
    else:
        return render(request, 'registration/confirmationfailed.html')



def registrationchoice(request):
    return render(request, 'user/registrationchoice.html')