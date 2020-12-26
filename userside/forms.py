from django import forms
from .models import order

class CreateOrderForm(forms.ModelForm):
	class Meta:
		model = order
		fields = '__all__'