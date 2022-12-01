from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from MainApp.models import Contact

# Create your views here.
#it's a request handler that handles the requests 

# def main_page(request):
#     conts= Contact.objects.all()
#     return render (request,"main.html",{'conts':conts})

class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
def contact(request):
    return render (request, "contact.html")

def about(request):
    return render (request, "about.html")

def services(request):
    return render (request, "services.html")

def term(request):
    return render (request, "term.html")