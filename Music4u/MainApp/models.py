from django.db import models

# Create your models here.

class Contact(models.Model):
   name= models.CharField(max_length=120)
   email= models.CharField(max_length=120)
   phone= models.CharField(max_length= 20)
   desc=  models.TextField()


   def __str__(self):
      return self.name

