from django.urls import path,include
from myapp.views import *

urlpatterns=[

path('myapp/',include('myapp.urls')),


]