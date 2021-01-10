from django.shortcuts import render, reverse
from .forms import UserRegistrationForm, ProfessionalUserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def loginpage(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user.is_active:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(request, messages.INFO, 'Account not active')
    else:
        messages.add_message(request, messages.INFO, 'Invalid login')
    
    return render(request, 'user/login.html')

    return render(request, 'user/login.html')


def usersignuppage(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'user/login.html')
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

