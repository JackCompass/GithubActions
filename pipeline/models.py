from django.db import models
from django.forms import ModelForm

class RegisteredUsers(models.Model):
	username = models.CharField(max_length = 100)
	age = models.PositiveIntegerField()
	country = models.CharField(max_length = 100)
	
class RegisteredUsersForms(ModelForm):
	"""Generating form of above model"""
	class Meta:
		model = RegisteredUsers
		fields = ['username', 'age', 'country']