from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def car(request):
    return render(request,'car.html')

def nuts(request):
    return render(request,'nuts.html')

def fruits(request):
    return HttpResponse('in fruits have good vitamin')




 