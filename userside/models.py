from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.model import User
# Create your models here.

class order(models.Model):
	user = 
	paper_sizes = (
			('a4','a4'),
			('a5','a5'),
			('b5','b5'),
			('b4','b4')
		)
	bending_type = (
			('','')
		)
	pdf_file = models.FileField(upload_to='pdf_files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','doc'])])
	paper_size = models.CharField(max_length=300,choices = paper_sizes,default='a4')
