from django.shortcuts import render,redirect
from .forms import UserRegisterForm,SetProfileForm,SetFaLForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.

class ChangePass(PasswordChangeView):
	template_name = 'users/password_change.html'
	success_url = reverse_lazy('userside:dashboard')

	def form_valid(self,form):
		messages.success(self.request,'your password has been changed')
		return super().form_valid(form)


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
		if request.method == 'POST':
			form_1 = SetProfileForm(request.POST,instance=request.user.profile)
			form_2 = SetFaLForm(request.POST,instance=request.user)
			if form_1.is_valid() and form_2.is_valid():
				form_1.save()
				form_2.save()
				messages.success(request,'your profile has been set')
				return redirect('userside:dashboard')
			else:
				messages.success(request,'error try agine later')
				return redirect('setprofile')
		else:
			form_1 = SetProfileForm(instance=request.user.profile)
			form_2 = SetFaLForm(instance=request.user)
			context = {'form_1':form_1,'form_2':form_2}
			return render(request,'users/set_profile.html',context)