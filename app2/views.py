from django.shortcuts import render

# Create your views here.

def fruits(request):
    return render(request,'fruits.html')

def monkey(request):
    return render(request,'monkey.html')

from django.http import HttpResponse

def box(request):
    return HttpResponse('hello')
