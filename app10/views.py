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
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def blog_details(request):
	return render(request,'blog_details.html')

def blog(request):
	return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')


def admin_contacts(request):
	if request.method == "POST":
		cname=request.POST['name']
		cemail=request.POST['email']
		cmessage=request.POST['message']
		cphonenumber=request.POST['phonenumber']
		add=contact_tb(name=cname,email=cemail,phonenumber=cphonenumber,message=cmessage)
		add.save()
		x = ''.join(random.choices(cname + string.digits, k=8))
		y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
		subject = 'welcome to aanamaya hospital'
		message = f'Hi {cname}, thank you for visiting aanamaya hospital . '
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [cemail, ] 
		send_mail( subject, message, email_from, recipient_list )
		return render(request,"admin/index.html")
	else:
	    return render(request,'admin/contacts.html')

# def doctor_details(request):
# 	return render(request,'doctor_details.html')

def doctor(request):
	data=doctor_tb.objects.all()
	return render(request,'doctor.html',{'data':data})

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
	

def admin_login(request):
	if request.method == "POST":
		cemail=request.POST['email']
		cpassword=request.POST['password']
		check=reg_tb.objects.filter(email=cemail)
		if check:
			for x in check:
				request.session['id']=x.id
				request.session['email']=x.email
			return render(request,'admin/index.html',{'success':"Successfully logined"})
		else:
		    return render(request,'admin/login.html',{'error':'invalid details '})
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
		    return render(request,'admin/register.html',{'success':"Successfully registered"})
	else:
	    return render(request,'admin/register.html')
	
def admin_logout(request):
	if request.session.has_key("id"):
		del request.session['id']
		del request.session['email']
	return HttpResponseRedirect('/admin_login/')

def admin_forms(request):
	if request.method == "POST":
		cdepartment=request.POST['department']
		cdescription=request.POST['description']
		check=service_tb.objects.filter(department=cdepartment)
		if check:
			return render(request,'admin/forms.html',{'error':'Already Data Saved'})
		else:
		    add=service_tb(department=cdepartment,description=cdescription)
		    add.save()
		    return render(request,'admin/index.html',{'success':"Successfully Data Saved"})
	else:
		return render(request,'admin/forms.html')

def admin_table(request):
	data=service_tb.objects.all()
	return render(request,'admin/table.html',{'details':data})

def admin_service_update(request):
	if request.method == "POST":
		cdepartment=request.POST['department']
		cdescription=request.POST['description']
		serviceid=request.GET['uid']
		# imgval=request.POST['imgup']
		# if imgval =="yes":

		# 	cimage=request.FILES['image']
		# 	oldrec=pro_tb.objects.filter(id=prdid)
		# 	updrec=pro_tb.objects.get(id=prdid)
		# 	for x in oldrec:
		# 		imgurl=x.image.url
		# 		pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
		# 		if os.path.exists(pathtoimage):
		# 			os.remove(pathtoimage)
		# 			print('Successfully deleted')
		# 	updrec.image=cimage
		# 	updrec.save()

		add=service_tb.objects.filter(id=serviceid).update(department=cdepartment,description=cdescription)
		return HttpResponseRedirect('/admin_table/')
	else:
		serviceid=request.GET['uid']
		data=service_tb.objects.filter(id=serviceid)
		return render(request,'admin/service_update.html',{'details':data})

def admin_service_delete(request):
    serviceid=request.GET['uidd']
    # oldrec=serviceid.objects.filter(id=serviceid)
    # for x in oldrec:
    # 	imgurl=x.image.url
    # 	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
    # 	if os.path.exists(pathtoimage):
    # 		os.remove(pathtoimage)
    data=service_tb.objects.filter(id=serviceid).delete()
    return HttpResponseRedirect('/admin_table/')

def admin_docforms(request):
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

def admin_doctables(request):
	data=doctor_tb.objects.all()
	return render(request,'admin/doctables.html',{'details':data})

def admin_service_update(request):
	if request.method == "POST":
		cdescription=request.POST['description']
		serviceid=request.GET['uid']
		# imgval=request.POST['imgup']
		# if imgval =="yes":

		# 	cimage=request.FILES['image']
		# 	oldrec=pro_tb.objects.filter(id=prdid)
		# 	updrec=pro_tb.objects.get(id=prdid)
		# 	for x in oldrec:
		# 		imgurl=x.image.url
		# 		pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
		# 		if os.path.exists(pathtoimage):
		# 			os.remove(pathtoimage)
		# 			print('Successfully deleted')
		# 	updrec.image=cimage
		# 	updrec.save()

		add=service_tb.objects.filter(id=serviceid).update(department=cdepartment,description=cdescription)
		return HttpResponseRedirect('/admin_table/')
	else:
		serviceid=request.GET['uid']
		data=service_tb.objects.filter(id=serviceid)
		return render(request,'admin/service_update.html',{'details':data})

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
    return HttpResponseRedirect('/admin_doctable/')





