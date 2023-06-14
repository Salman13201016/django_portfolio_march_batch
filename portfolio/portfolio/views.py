
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect

from . import models
from .models import About

def index(request):
    sum = 10 + 20
    return render(request,'index.html')
def aboutindex(request):
    data = About.objects.all()
    all_data ={"about_data":data}
    return render(request,'admin/about.html',context=all_data)

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

    return redirect('/admin/about/')
    # return render(request,'admin/about.html')

def edit_form(request, id):
    # data = get_object_or_404(About, id=id)
    d = {"id":id}
    # print(data)
    return render(request,'admin/edit_about.html',context=d)

def update(request):
    id= request.POST.get('id')
    data = get_object_or_404(About, id=id)
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    bg = request.POST.get('bg')
    fb = request.POST.get('fb')
    # about = models.About()
    data.name = name
    data.phone = phone
    data.email = email
    data.bg = bg
    data.fb = fb
    data.save()

    # print(data)
    return redirect('/admin/about/')

def delete(request, id):
    data = get_object_or_404(About, id=id)
    data.delete()
    # print(data)
    return redirect('/admin/about/')