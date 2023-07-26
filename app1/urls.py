from django.urls import path
from app1.views import *
app_name='first'

urlpatterns=[
    path('carrot/',carrot,name='carrot'),
    path('banana/',banana,name='banana'),
    path('pen/',pen,name='pen'),
]