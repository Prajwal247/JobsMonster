from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

# Create your views here.
def agriculture(request):
    userss  = get_user_model().objects.filter(Specialization='Agriculture,Food and Natural Resources').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})
    
def architecture(request):
    userss  = get_user_model().objects.filter(Specialization='Architecture and COnstruction').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def technology(request):
    userss  = get_user_model().objects.filter(Specialization='Technology and Communications').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def sales(request):
    userss  = get_user_model().objects.filter(Specialization='Sales and Marketing').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def business(request):
    userss  = get_user_model().objects.filter(Specialization='Business Management and Administration').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def Education(request):
    userss  = get_user_model().objects.filter(Specialization='Education and Training').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def Health(request):
    userss  = get_user_model().objects.filter(Specialization='Health Science').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def Law(request):
    userss  = get_user_model().objects.filter(Specialization='Law and Pulblic Safety').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def transportation(request):
    userss  = get_user_model().objects.filter(Specialization='Transportation').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})

def It(request):
    userss  = get_user_model().objects.filter(Specialization='Information Technology').order_by('?')
    paginator_user = Paginator(userss,4)
    page_number_users = request.GET.get('page')
    users = paginator_user.get_page(page_number_users)
    return render(request, 'category.html',{"users":users})