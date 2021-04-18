from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	username = models.CharField(max_length = 200, null = True)
	name = models.CharField(max_length = 200, null = True, blank=True)
	phone = models.CharField(max_length = 200, null = True, blank=True)
	email = models.CharField(max_length = 200, null = True, blank=True)
	profile_pic = models.ImageField(default ="logo.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name


class Survey(models.Model):
	name = models.CharField(max_length = 200, null = True)
	
	def __str__(self):
		return self.name

	customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)


class Record(models.Model):
	survey_id = models.CharField(max_length = 200, null = True)
	name = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200, null = True)
	osat = models.CharField(max_length = 200, null = True)
	comment = models.CharField(max_length = 1000, null = True)
	user = models.ForeignKey(User, default=None, on_delete = models.SET_NULL, null=True)
	customer = models.ForeignKey(Customer, default=None, on_delete = models.SET_NULL, null=True)
	def __str__(self):
		return self.survey_id

	