from django.shortcuts import render

# Create your views here.

def carrot(request):
    return render(request,'carrot.html')


def banana(request):
    return render(request,'banana.html')

from django.http import HttpResponse

def pen(request):
    return HttpResponse('hi hello')
