from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import csv,io

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
	context={}
	return render(request,'word/dashboard.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')	

def viewResponse(request):
	user_loggedin = request.user
	parent = Customer.objects.filter(username= user_loggedin)
	if parent:
		parent = Customer.objects.get(username= user_loggedin)
		child = parent.record_set.all()
		records_list = list(child)
		allrecords = []
		for i in records_list:
			print (i)
			allrecords.append(Record.objects.get(survey_id=str(i)))
		print (allrecords)
		records=allrecords
		context={'records':records}
		return render(request,'word/responses.html', context)
	else:
		context={}
		return render(request,'word/responses.html', context)

def uploadData(request):
	if len(request.FILES) != 0:
		csv_file = request.FILES['file']

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
					survey_id = column[0],
					name = column[1],
					email = column[2],
					osat = column[3],
					comment = column[4],
					customer = customer_addingrecord,
					user = request.user
				)
		records = Record.objects.all()
		context={'records':records}
		return render(request,'word/responses.html', context)
	else:
		context={}
		return redirect('responses')