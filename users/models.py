from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.


class UserRegisterForm(UserCreationForm):
	class Meta:
		model