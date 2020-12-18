from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import order
# Create your views here.

def index(request):
	return render(request,'userside/index.html')

@login_required
def dashboard(request):
	if request.user.profile.phone_number == '':
		return redirect('setprofile')
	return render(request,'userside/dashboard.html')