from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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