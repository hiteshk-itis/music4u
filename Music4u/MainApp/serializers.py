from . import models
from rest_framework import serializers



class ContactSerializer(serializers.ModelSerializer):	
	class Meta:
		model = models.Contact
		fields = ('name','email','phone','desc')