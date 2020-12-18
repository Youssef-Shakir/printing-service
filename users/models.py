from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phone_number = PhoneNumberField(null=False, blank=False, unique=False)
	address = models.CharField(max_length=250)

	def __str__(self):
		return f'{self.user.username} profile'

