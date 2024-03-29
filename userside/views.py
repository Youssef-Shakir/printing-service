from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import order
from .forms import CreateOrderForm
# Create your views here.

def index(request):
	return render(request,'userside/index.html')

@login_required
def dashboard(request):
	if request.user.profile.phone_number == '':
		return redirect('setprofile')
	elif request.user.first_name == '':
		return redirect('setprofile')
	else:
		return render(request,'userside/dashboard.html')

def createorderview(request):
	if request.method == 'POST':
		pass

	else:
		form = CreateOrderForm()
		context = {'form':form}
		return render(request,'userside/createorder.html',context)
