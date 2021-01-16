from django.shortcuts import render

from . import forms
# Create your views here.

def hiring(request):
    form = forms.HiringForm()
    return render(request, 'hiring/hiringform.html',{'form':form})