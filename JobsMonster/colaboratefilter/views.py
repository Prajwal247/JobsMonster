from django.shortcuts import render
from hiring.models import Jobpost, Applicants
from User.models import User 
from django.core.paginator import Paginator
from .models import recommendation 
# Create your views here.
def job_recommend(request):
    page = request.GET.get("page", 1)
    user_id = request.session.get("user_id")
    cache_key = ITEM_CACHE.format(user_id=user_id)
    job_list = cache.get(cache_key)
    job = Jobpost
    if job is None:
        job_list = recommendation
        cache.set(cache_key, job_list, 60 * 5)
    
    job = job_paginator(job_list, page)
    path = request.path
    title = "Jobs"
    return render(
        request, "user/job.html", {"jobs": jobs, "path": path, "title": title}
    )