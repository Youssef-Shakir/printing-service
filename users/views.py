from django.shortcuts import render,redirect
from .forms import UserRegisterForm,SetProfileForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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
@login_required
def setprofile(request):
	if request.user.profile.phone_number == '':
		print('ksamk')
		if request.method == 'POST':
			form = SetProfileForm(request.POST,instance=request.user.profile)
			if form.is_valid():
				form.save()
				return redirect('userside:dashboard')
		else:
			form = SetProfileForm()
			context = {'form':form}
			return render(request,'users/set_profile.html',context)
	else:
		return redirect('userside:dashboard')