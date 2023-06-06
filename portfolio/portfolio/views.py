
from django.http import HttpResponse
from django.shortcuts import render

from . import models

def index(request):
    sum = 10 + 20
    return render(request,'index.html')
def aboutindex(request):
    sum = 10 + 20
    return render(request,'admin/about.html')

def store(request):
    # sum = 10 + 20
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    bg = request.POST.get('bg')
    fb = request.POST.get('fb')
    about = models.About()
    about.name = name
    about.phone = phone
    about.email = email
    about.bg = bg
    about.fb = fb
    about.save()

    return HttpResponse(fb)
    # return render(request,'admin/about.html')