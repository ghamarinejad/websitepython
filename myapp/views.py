from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    return render(request= request,template_name= 'home.html') 



def about_view(request):
      return render(request=request,template_name='about.html')  



def register_view(request):
      return render(request=request,template_name='register.html') 