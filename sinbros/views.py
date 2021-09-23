# i have created this page - sumit singh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<a href="https://www.sinbros.com">Sinbros</a>''')
