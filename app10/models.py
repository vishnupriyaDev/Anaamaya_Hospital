from django.db import models

# Create your models here.
class contact1_tb(models.Model):
	name=models.CharField(max_length=225)
	email=models.CharField(max_length=225)
	phonenumber=models.CharField(max_length=225)
	message=models.TextField()

class contact_tb(models.Model):
	name=models.CharField(max_length=225)
	email=models.CharField(max_length=225)
	phonenumber=models.CharField(max_length=225)
	message=models.TextField()

class reg_tb(models.Model):
	email=models.CharField(max_length=225)
	password=models.CharField(max_length=225)
	confirmpassword=models.CharField(max_length=225)

class service_tb(models.Model):
	department=models.CharField(max_length=225)
	image=models.ImageField(upload_to="service/")
	description=models.TextField()

class doctor_tb(models.Model):
	doctorname=models.CharField(max_length=225)
	image=models.ImageField(upload_to="imagefiles/")
	department=models.ForeignKey(service_tb, on_delete=models.CASCADE)
	qualification=models.CharField(max_length=225)

class appoinment_tb(models.Model):
	docid=models.ForeignKey(doctor_tb, on_delete=models.CASCADE)
	name=models.CharField(max_length=225)
	email=models.CharField(max_length=225)
	phonenumber=models.CharField(max_length=225)
	date=models.CharField(max_length=225)
	
	
