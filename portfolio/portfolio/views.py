
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    sum = 10 + 20
    return render(request,'index.html')