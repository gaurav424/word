from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	username = models.CharField(max_length = 200, null = True)
	name = models.CharField(max_length = 200, null = True, blank=True)
	phone = models.CharField(max_length = 200, null = True, blank=True)
	email = models.CharField(max_length = 200, null = True, blank=True)
	profile_pic = models.ImageField(default ="logo.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add = True)
	org = models.ForeignKey(Organization, default=1, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name


class Survey(models.Model):
	name = models.CharField(max_length = 200, null = True, default=1)
	org = models.ForeignKey(Organization, default=None, on_delete = models.SET_NULL, null=True)
	
	def __str__(self):
		return self.name

	

class Record(models.Model):
	PERMSSION_TO_CONTACT = (
	('Yes','Yes'),
	('No','No'),
	)
	surveyid = models.AutoField(primary_key=True, verbose_name = 'Survey ID', default = None)
	name = models.CharField(max_length = 200, null = True, blank=True)
	mobile = models.CharField(max_length = 10, null = True, blank=True)
	email = models.CharField(max_length = 200, null = True, blank=True)
	osat = models.CharField(max_length = 200, null = True)
	rsn_for_score = models.CharField(max_length = 1000, null = True, blank=True)
	permission_to_contact = models.CharField(max_length = 200, null = True, choices = PERMSSION_TO_CONTACT, blank=True)
	#user = models.ForeignKey(User, default=None, on_delete = models.SET_NULL, null=True)
	#customer = models.ForeignKey(Customer, default=None, on_delete = models.SET_NULL, null=True)
	survey = models.ForeignKey(Survey, default=1, on_delete = models.SET_NULL, null=True, blank=True)

	def __str__(self):
		survey_id = str(self.surveyid)
		#return  survey_id+" - "+self.name
		return survey_id
