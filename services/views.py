from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'services/web-development.html')

def mobile_application(request):
    return render(request, 'services/mobile-application.html')

def desktop_application(request):
    return render(request, 'services/desktop-application.html')

def digital_marketing(request):
    return render(request, 'services/digital-marketing.html')
# Create your views here.
