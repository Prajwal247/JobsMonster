from django.shortcuts import render, redirect

from . import forms
# Create your views here.

def hiring(request):
    form = forms.HiringForm()
    return render(request, 'hiring/hiringform.html',{'form':form})

def postjob(request):
    form = forms.PostJobForm()
    if request.method == 'POST':

        form = forms.PostJobForm(request.POST)
        form.instance.posted_by = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'hiring/postjob.html', {'form':form})