
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from app10.models import *
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail
import datetime

# Create your views here.
def index(request):
	data=doctor_tb.objects.all()[:4]
	return render(request,'index.html',{'data':data})

def about(request):
	return render(request,'about.html')

def blog_details(request):
	return render(request,'blog_details.html')

def blog(request):
	return render(request,'blog.html')

def contact(request):
	if request.method == "POST":
		cname=request.POST['name']
		cemail=request.POST['email']
		cmessage=request.POST['message']
		cphonenumber=request.POST['phonenumber']
		check=contact1_tb.objects.filter(name=cname,email=cemail,phonenumber=cphonenumber,message=cmessage)
		if check:
			return render(request,'index.html',{'error':'Already registered'})
		else:
			add=contact1_tb(name=cname,email=cemail,phonenumber=cphonenumber,message=cmessage)
			add.save()
			x = ''.join(random.choices(cname + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'Welcome to Anaamaya Hospital'
			message = f'Hi {cname}, Thank you for valueble feeback. '
			email_from = settings.EMAIL_HOST_USER 
			recipient_list = [cemail, ] 
			send_mail( subject, message, email_from, recipient_list )
			asubject = 'Contact form '
			amessage = f' A message from  {cname}, message is {cmessage}, contact number is {cphonenumber} '
			aemail_from = settings.EMAIL_HOST_USER 
			arecipient_list = [settings.EMAIL_HOST_USER , ] 
			send_mail( asubject, amessage, aemail_from, arecipient_list )
			return render(request,"index.html" ,{'success':"Thank You For Submitting"})
	else:
		return render(request,'contact.html')




# def doctor_details(request):
# 	return render(request,'doctor_details.html')

def doctor(request):
	data=doctor_tb.objects.all()
	return render(request,'doctor.html',{'data':data})

def appoinment(request):
	appoinment=doctor_tb.objects.all()
	if request.method == "POST":
		did=request.GET['did']
		cname=request.POST['name']
		cemail=request.POST['email']
		cphonenumber=request.POST['phone']
		cdate=request.POST['date']
		# cdoctorname=request.POST['doctorname']
		did=doctor_tb.objects.get(id=did )
		check=appoinment_tb.objects.filter(name=cname,email=cemail,phonenumber=cphonenumber,date=cdate,docid=did)
		if check:
			return render(request,'doctor.html',{'error':'Already Data Saved','details':appoinment})
		else:
	 		add=appoinment_tb(name=cname,email=cemail,phonenumber=cphonenumber,date=cdate,docid=did)
	 		add.save()
	 		x = ''.join(random.choices(cname + string.digits, k=8))
	 		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
	 		subject = 'welcome to Anaamaya hospital Appoinment'
	 		message = f'Hi {cname}, Thank you for visiting Anaamaya Hospital . '
	 		email_from = settings.EMAIL_HOST_USER 
	 		recipient_list = [cemail, ] 
	 		send_mail( subject, message, email_from, recipient_list )
	 		asubject = 'An appoinment has been registered'
	 		amessage = f'A appoinment from  {cname}, date is {cdate}, contact number is {cphonenumber} '
	 		aemail_from = settings.EMAIL_HOST_USER 
	 		arecipient_list = [settings.EMAIL_HOST_USER, ] 
	 		send_mail( asubject, amessage, aemail_from, arecipient_list )
	 		data=doctor_tb.objects.all()[:4]
	 		return render(request,'index.html',{'success':"Successfully Booked",'data':data })
	else:
		return render(request,'doctor.html',{'details':appoinment})


def faq(request):
	return render(request,'faq.html')

def giving_back(request):
	return render(request,'giving_back.html')

def login(request):
	return render(request,'login.html')

def mission_vission(request):
	return render(request,'mission_vission.html')

def privacy(request):
	return render(request,'privacy.html')

def refund_policy(request):
	return render(request,'refund_policy.html')

def registration(request):
	return render(request,'registration.html')

# def service_details(request):
# 	return render(request,'service_details.html')

# def service_two(request):
# 	return render(request,'service_two.html')

def service(request):
	data=service_tb.objects.all()
	return render(request,'service.html',{'data':data})

def term_of_service(request):
	return render(request,'term_of_service.html')

def timeline(request):
	return render(request,'timeline.html')

#############################################################################################################
def admin_index(request):
	if request.session.has_key("id"):
		return render(request,'admin/index.html')
	else:
		return HttpResponseRedirect('/admin_login/')

# def admin_contacts(request):
# 	if request.method == "POST":
# 		cname=request.POST['name']
# 		cemail=request.POST['email']
# 		cmessage=request.POST['message']
# 		cphonenumber=request.POST['phonenumber']
# 		check=contact_tb.objects.filter(name=cname,email=cemail,phonenumber=cphonenumber,message=cmessage)
# 		if check:
# 			return render(request,'index.html',{'error':'Already registered'})
# 		else:
# 			add=contact_tb(name=cname,email=cemail,phonenumber=cphonenumber,message=cmessage)
# 			add.save()
# 			x = ''.join(random.choices(cname + string.digits, k=8))
# 			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
# 			subject = 'welcome to aanamaya hospital'
# 			message = f'Hi {cname}, thank you for visiting aanamaya hospital . '
# 			email_from = settings.EMAIL_HOST_USER 
# 			recipient_list = [cemail, ] 
# 			send_mail( subject, message, email_from, recipient_list )
# 			return render(request,"admin/index.html",{'success':"Successfully registered"})
# 	else:
# 		return render(request,'admin/contacts.html')
	

def admin_login(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		check=reg_tb.objects.filter(email=cemail,password=cpassword)
		if check:
			for x in check:
				request.session['id']=x.id
				request.session['email']=x.email
			return render(request,'admin/index.html',{'success':"Successfully logined"})
		else:
		    return render(request,'admin/login.html',{'error':"Creditionals invalid"})
	else:
		return render(request,'admin/login.html')
	

def admin_register(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		cconfirmpassword=request.POST['confirmpassword']
		check=reg_tb.objects.filter(email=cemail)
		if check:
			return render(request,'admin/register.html',{'error':'Already registered'})
		else:
		    add=reg_tb(email=cemail,password=cpassword,confirmpassword=cconfirmpassword)
		    add.save()
		    return render(request,'admin/index.html',{'success':"Successfully registered"})
	else:
	    return render(request,'admin/register.html')
	
def admin_logout(request):
	if request.session.has_key("id"):
		del request.session['id']
		del request.session['email']
	return HttpResponseRedirect('/admin_login/')

def admin_forms(request):
	if request.session.has_key("id"):
		if request.method == "POST":
			cdepartment=request.POST['department']
			cimage=request.FILES['image']
			cdescription=request.POST['description']
			check=service_tb.objects.filter(department=cdepartment)
			if check:
				return render(request,'admin/forms.html',{'error':'Already Data Saved'})
			else:
				add=service_tb(department=cdepartment,image=cimage,description=cdescription)
				add.save()
				return render(request,'admin/index.html',{'success':"Successfully Data Saved"})
		else:
			return render(request,'admin/forms.html')
	else:
		return HttpResponseRedirect('/admin_login/')


def admin_table(request):
	if request.session.has_key("id"):
		data=service_tb.objects.all()
		return render(request,'admin/table.html',{'details':data})
	else:
		return HttpResponseRedirect('/admin_login/')


def admin_appoinment_table(request):
	if request.session.has_key("id"):
		data=appoinment_tb.objects.all()
		return render(request,'admin/appoinment_table.html',{'details':data})
	else:
		return HttpResponseRedirect('/admin_login/')

def admin_service_update(request):
	if request.method == "POST":
		cdepartment=request.POST['department']
		cdescription=request.POST['description']
		serviceid=request.GET['uid']
		imgval=request.POST['imgup']
		if imgval =="yes":

			cimage=request.FILES['image']
			oldrec=service_tb.objects.filter(id=serviceid)
			updrec=service_tb.objects.get(id=serviceid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image=cimage
			updrec.save()

		add=service_tb.objects.filter(id=serviceid).update(department=cdepartment,description=cdescription)
		return HttpResponseRedirect('/admin_table/')
	else:
		serviceid=request.GET['uid']
		data=service_tb.objects.filter(id=serviceid)
		return render(request,'admin/service_update.html',{'details':data})

def admin_service_delete(request):
    serviceid=request.GET['uidd']
    oldrec=service_tb.objects.filter(id=serviceid)
    for x in oldrec:
    	imgurl=x.image.url
    	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
    	if os.path.exists(pathtoimage):
    		os.remove(pathtoimage)
    data=service_tb.objects.filter(id=serviceid).delete()
    return HttpResponseRedirect('/admin_table/')

def admin_docforms(request):
	if request.session.has_key("id"):
		data=service_tb.objects.all()
		if request.method == "POST":
			cdoctorname=request.POST['name']
			cimage=request.FILES['image']
			cdepartment=request.POST['department']
			cdepartment=service_tb.objects.get(id=cdepartment)
			cqualification=request.POST['qualification']
			check=doctor_tb.objects.filter(doctorname=cdoctorname)
			if check:
				return render(request,'admin/docforms.html',{'error':'Already Data Saved','details':data})
			else:
				add=doctor_tb(doctorname=cdoctorname,image=cimage,department=cdepartment,qualification=cqualification)
				add.save()
				return render(request,'admin/index.html',{'success':"Successfully Data Saved"})
		else:
			return render(request,'admin/docforms.html' ,{'details':data})
	else:
		return HttpResponseRedirect('/admin_login/')


def admin_doctables(request):
	if request.session.has_key("id"):
		data=doctor_tb.objects.all()
		return render(request,'admin/doctables.html',{'details':data})
	else:
		return HttpResponseRedirect('/admin_login/')


def admin_usertables(request):
	if request.session.has_key("id"):
		data=contact1_tb.objects.all()
		return render(request,'admin/usertables.html',{'details':data})
	else:
		return HttpResponseRedirect('/admin_login/')



# def admin_service_update(request):
# 	if request.method == "POST":
# 		cdescription=request.POST['description']
# 		serviceid=request.GET['uid']
# 		# imgval=request.POST['imgup']
# 		# if imgval =="yes":

# 		# 	cimage=request.FILES['image']
# 		# 	oldrec=pro_tb.objects.filter(id=prdid)
# 		# 	updrec=pro_tb.objects.get(id=prdid)
# 		# 	for x in oldrec:
# 		# 		imgurl=x.image.url
# 		# 		pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
# 		# 		if os.path.exists(pathtoimage):
# 		# 			os.remove(pathtoimage)
# 		# 			print('Successfully deleted')
# 		# 	updrec.image=cimage
# 		# 	updrec.save()

# 		add=service_tb.objects.filter(id=serviceid).update(department=cdepartment,description=cdescription)
# 		return HttpResponseRedirect('/admin_table/')
# 	else:
# 		serviceid=request.GET['uid']
# 		data=service_tb.objects.filter(id=serviceid)
# 		return render(request,'admin/service_update.html',{'details':data})

def admin_docform_update(request):
	data=service_tb.objects.all()
	if request.method == "POST":
		cdoctorname=request.POST['name']
		
		cdepartment=request.POST['department']
		cdepartment=service_tb.objects.get(id=cdepartment )
		cqualification=request.POST['qualification']
		serviceid=request.GET['uid']
		imgval=request.POST['imgup']
		if imgval =="yes":
			cimage=request.FILES['image']
			oldrec=doctor_tb.objects.filter(id=serviceid)
			updrec=doctor_tb.objects.get(id=serviceid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image=cimage
			updrec.save()

		add=doctor_tb.objects.filter(id=serviceid).update(doctorname=cdoctorname,department=cdepartment,qualification=cqualification)
		return HttpResponseRedirect('/admin_doctables/')
	else:
		serviceid=request.GET['uid']
		data=doctor_tb.objects.filter(id=serviceid)
		return render(request,'admin/docform_update.html',{'details':data})
		
def admin_docform_delete(request):
    serviceid=request.GET['uidd']
    oldrec=doctor_tb.objects.filter(id=serviceid)
    for x in oldrec:
    	imgurl=x.image.url
    	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
    	if os.path.exists(pathtoimage):
    		os.remove(pathtoimage)
    data=doctor_tb.objects.filter(id=serviceid).delete()
    return HttpResponseRedirect('/admin_doctables/')





