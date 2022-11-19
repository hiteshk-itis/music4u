from django.db import models

# Create your models here.

class Register(models.Model):
    username= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    password= models.CharField(max_length= 20)
    password2=  models.TextField()
    date= models.DateField()

class Login(models.Model):
    username= models.CharField(max_length=120)
    password= models.CharField(max_length= 20)
    