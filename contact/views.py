from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from .models import Contact

def index(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        mobile = request.POST.get('mobile','')
        email = request.POST.get('email','')
        sub = request.POST.get('sub','')
        msg = request.POST.get('msg','')

        contact = Contact(contact_name=name,contact_mobile=mobile,contact_email=email,contact_sub=sub,contact_msg=msg)
        contact.save()
        messages.success(request, 'Message Sent Successfully...')
    return render(request, 'contact/contact.html')
# Create your views here.
