from django import forms
from .models import order
from phonenumber_field.formfields import PhoneNumberField
from PyPDF2 import PdfFileReader
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = order
        widgets = {
        'paper_size' : forms.RadioSelect(),
        'location' : forms.TextInput(attrs={'placeholder':'ksamnk'})
        }
        fields = ['pdf_file','paper_size','bending_type','phone_number','location','notes']
