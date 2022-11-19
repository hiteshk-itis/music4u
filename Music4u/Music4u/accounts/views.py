from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        username= request.POST['name']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['pass2']
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "USERNAME TAKEN")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "EMAIL TAKEN")
            else:
                user = User.objects.create_user(username=username, password=password, email=email,)
                user.save();
                messages.success(request, "USER CREATED")
        else: 
            print('password no matching')
        return redirect("/")        
    return render (request, "register.html")

def login(request):
    if request.method=="POST":
        username = request.POST['username']
    return render (request, "login.html")