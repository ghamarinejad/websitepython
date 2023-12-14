from django.urls import path
from myapp.views import *

urlpatterns = [

path('home',home_view),
path('about',about_view),
path('register',register_view),

]