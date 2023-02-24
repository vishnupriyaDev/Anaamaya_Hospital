from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from app10.models import *

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

def doctor_details(request):
	return render(request,'doctor_details.html')

def doctor(request):
	return render(request,'doctor.html')

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

def service_details(request):
	return render(request,'service_details.html')

def service_two(request):
	return render(request,'service_two.html')

def service(request):
	return render(request,'service.html')

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