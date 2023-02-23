from django.db import models

# Create your models here.
class reg_tb(models.Model):
	email=models.CharField(max_length=225)
	password=models.CharField(max_length=225)
	confirmpassword=models.CharField(max_length=225)
