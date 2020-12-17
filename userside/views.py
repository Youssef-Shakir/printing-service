from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,'userside/index.html')


def dashboard(request):
	return render(request,'userside/dashboard.html')