from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext

import csv,io
import json

from .models import *
from .forms import *

# Create your views here.
def registerPage(request):
	form = CreateUserForm()
	form2 = CustomerForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			
			form_username = form.cleaned_data.get('username')
			customer = Customer.objects.filter(username = form_username)
			if not customer:
				messages.info(request, form_username + ' is not authorized')
			else:
				user = form.save()
				username = form.cleaned_data.get('username')
			
				messages.success(request, 'Account was created for ' + username)
				return redirect('login')

	context = {'form':form}
	return render(request, 'word/register.html', context)


def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password is incorrect')

	context = {}
	return render(request, 'word/login.html', context)


def home(request):
	user_loggedin = request.user
	#total_records_received = survey_list.record_set.all().count()
	total_records_received=0
	context={'records_recieved':total_records_received}

	return render(request,'word/dashboard.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')	

def viewResponse(request):
	user_loggedin = request.user
	parent = Customer.objects.filter(username= user_loggedin)
	if parent:
		parent = Customer.objects.get(username= user_loggedin)
		org_id = parent.org.id
		survey_list = Survey.objects.filter(org = org_id)
		survey_list_id = []
		for i in survey_list:
			survey_list_id.append(i.id)
		#child = parent.record_set.all()
		#records_list = list(child)
		allrecords = []
		for i in survey_list_id:
			survey_name = Survey.objects.get(id = i)
			child = survey_name.record_set.all()
			records_list = list(child)
			for i in records_list:
				allrecords.append(Record.objects.get(surveyid=str(i)))
		records=allrecords
		print (records)
		context={'records':records}
		return render(request,'word/responses.html', context)
	else:
		context={}
		return render(request,'word/responses.html', context)

def uploadData(request):
	if len(request.FILES) != 0:
		csv_file = request.FILES['file']
		user_addingrecord = request.user
		customer_addingrecord = Customer.objects.get(username = user_addingrecord)

		if csv_file.name.endswith('.json'):

			with open("static/images/test_json_file_2.json") as f:
				data = json.load(f)
				data_dict = data['records']
				for key in data_dict:
					_, created = Record.objects.update_or_create(
					name = key['name'],
					email = key['email'],
					osat = key['osat'],
					comment = key['comment'],
					customer = customer_addingrecord,
					user = request.user
				)
			records = Record.objects.all()
			context={'records':records}
			return render(request,'word/responses.html', context)	


		if not csv_file.name.endswith('.csv'):
			messages.error(request, 'This is not a csv file')
		
		name=email=osat=comment = []
		data_set = csv_file.read().decode('UTF-8')
		io_string = io.StringIO(data_set)
		next(io_string)
		records = []
		user_addingrecord = request.user
		customer_addingrecord = Customer.objects.get(username = user_addingrecord)
		for column in csv.reader(io_string, delimiter = ',', quotechar = '"'):
			_, created = Record.objects.update_or_create(
					name = column[0],
					email = column[1],
					osat = column[2],
					comment = column[3],
					customer = customer_addingrecord,
					user = request.user
				)
		user_loggedin = request.user
		parent = Customer.objects.get(username = user_loggedin)
		child = parent.record_set.all()
		records_list = list(child)
		allrecords = []
		for i in records_list:
			allrecords.append(Record.objects.get(surveyid=str(i)))
		records=allrecords
		context={'records':records}
		return render(request,'word/responses.html', context)
	else:
		context={}
		return redirect('responses')


def testSurvey(request):
	form = TestSurvey()
	context={}
	if request.method == 'POST':
		form = TestSurvey(request.POST)
		print(form.errors.as_data())
		name = form.cleaned_data.get('name')
		osat = form.cleaned_data.get('osat')
		mobile = form.cleaned_data.get('mobile')
		email = form.cleaned_data.get('email')
		rsn_for_score = form.cleaned_data.get('rsn_for_score')
		permission_to_contact = form.cleaned_data.get('permission_to_contact')
		comment = form.cleaned_data.get('comment')
		print("name = ",name)
		print("osat = ",osat)
		print("mobile = ", mobile)
		print("email = ", email)
		print("rsn_for_score = ", rsn_for_score)
		print("permission_to_contact = ", permission_to_contact)
		if form.is_valid():
			form.save()
		return render(request,'word/post_survey.html', context)
		#return render('word/post_survey.html', context,  RequestContext(request))

	context={'form':form}
	return render(request,'word/test_survey.html', context)
	#return render('word/test_survey.html', context,  RequestContext(request))
