from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from MainApp.models import Contact
from django.contrib import messages
# Create your views here.
#it;s a request handler that handles the requests 

def main_page(request):
    conts= Contact.objects.all()
    return render (request,"main.html",{'conts':conts})

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc= desc, date=datetime.today())
        contact.save()
        messages.success(request, "your form have been submitted")
    return render (request, "contact.html")

def about(request):
    return render (request, "about.html")

def services(request):
    return render (request, "services.html")

def term(request):
    return render (request, "term.html")