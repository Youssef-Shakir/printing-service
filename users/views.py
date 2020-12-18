from django.shortcuts import render,redirect
from .forms import UserRegisterForm,SetProfileForm
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.


def registerview(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request,f'Hi {username} your account has been created now setup your profile')
			new_user = form.save()
			login(request,new_user)
			return redirect('setprofile')
	else:
		form = UserRegisterForm()
		return render(request,'users/register.html',{'form':form})

def setprofile(request):
	form = SetProfileForm()
	context = {'form':form}
	return render(request,'users/set_profile.html',context)