from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

def home_view(request):
   
    return render(request, 'homic/home_view.html')

def home_co(request):
    return redirect(reverse('home_view'))


