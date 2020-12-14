from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class order(models.Model):
	user_acount = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	paper_sizes = (
			('a4','a4'),
			('a5','a5'),
			('b5','b5'),
			('b4','b4')
		)
	bending_types = (
			('booklet','booklet'),
			('book','book'),
			('side clips','side clips'),
			('corner clips','corner clips'),
		)
	order_staties = (
			('pending','pending'),
			('working on','working on'),
			('deliverd','deliverd'),
			('complete','complete')
		)
	pdf_file = models.FileField(upload_to='pdf_files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','doc'])])
	paper_size = models.CharField(max_length=300,choices = paper_sizes,default='a4')
	bending_type = models.CharField(max_length=300,choices = bending_types,default='clips')
	data_orderd = models.DateTimeField(default=timezone.now)
	order_statis = models.CharField(max_length=300,choices = order_staties,default='pending')
	location = models.CharField(max_length=300,default='')
	notes = models.TextField(max_length=1000,default='')
