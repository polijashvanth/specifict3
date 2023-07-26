from django.urls import path
from app2.views import *
app_name='second'

urlpatterns=[
    path('fruits/',fruits,name='fruits'),
    path('monkey',monkey,name='monkey'),
    path('box/',box,name='box'),
]