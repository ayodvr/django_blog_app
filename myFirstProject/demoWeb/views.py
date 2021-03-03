from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexx(response):
    return HttpResponse("Hello World")

def anotherMethod(request):
    return render(request,'demoweb/index.html')