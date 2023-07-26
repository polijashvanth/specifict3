from django.urls import path
from app3.views import *
app_name='first'

urlpatterns=[
    path('car/',car,name='car'),
    path('nuts/',nuts,name='nuts'),
    path('fruits/',fruits,name='fruits'),
]