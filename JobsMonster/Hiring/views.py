from django.shortcuts import render

from . import forms
# Create your views here.

def hiring(request):
    form = forms.HiringForm()
    return render(request, 'hiring/hiringform.html',{'form':form})

def postjob(request):
    form = forms.PostJobForm()
    if request.method == 'POST':
        form = forms.PostJobForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'jobs/home.html')
    return render(request, 'hiring/postjob.html', {'form':form})