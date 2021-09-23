from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'about/about-us.html')

def our_experts(request):
    return render(request, 'about/our-experts.html')

def sumit_singh(request):
    return render(request, 'about/sumit-singh.html')

def chandani_singh(request):
    return render(request, 'about/chandani-singh.html')

def aman_singh(request):
    return render(request, 'about/aman-singh.html')

def vision_mission_values(request):
    return render(request, 'about/vision-mission-values.html')
# Create your views here.
