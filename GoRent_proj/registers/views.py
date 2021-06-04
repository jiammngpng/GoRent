from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
#from .forms import *
from database.models import *
	
# Create your views here.

class GoRentLoginOwnerPage(View):
	def get(self, request):
		return render(request, 'registers/loginOwner.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginOwner' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user_object = RentOwner.objects.filter(email = username)
				if(user_object.count() == 1 and user_object[0].password == password):
					return HttpResponse("Success") #PUT THE REDIRECTORY FOR THE OWNER MAINPAGE HERE
				else:
					return HttpResponse("Fail")

class GoRentLoginShareePage(View):
	def get(self, request):
		return render(request, 'registers/loginSharee.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post(self, request):
		if request.method == 'POST':
			if 'btnLoginSharee' in request.POST:
				username = request.POST.get("username")
				password = request.POST.get("password")
				user_object = Sharee.objects.get(email = username)
				if(user_object.count() == 1 and user_object[0].password == password):
					return HttpResponse("Success") #PUT THE REDIRECTORY FOR THE SHAREE MAINPAGE HERE
				else:
					return HttpResponse("Fail")


class GoRentOwnerRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/ownerRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post (self,request):
		ownerFirstName = request.POST.get("ownerFirstName")
		ownerLastName = request.POST.get("ownerLastName")
		ownerEmail = request.POST.get("ownerEmail")
		ownerPassword = request.POST.get("ownerPassword")
		ownerMobileNumber = request.POST.get("ownerMobileNumber")
		ownerBirthdate = request.POST.get("ownerBirthdate")
		
		obj = RentOwner(email = ownerEmail, firstname = ownerFirstName, lastname = ownerLastName, password = ownerPassword, contactnumber = ownerMobileNumber, birthday = ownerBirthdate)
		obj.save()
		return render(request, 'registers/loginOwner.html')

class GoRentShareeRegisterPage(View):	
	def get(self, request):
		return render(request, 'registers/shareeRegisterPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
	def post (self,request):
		shareeFirstName = request.POST.get("shareeFirstName")
		shareeLastName = request.POST.get("shareeLastName")
		shareeEmail = request.POST.get("shareeEmail")
		shareePassword = request.POST.get("shareePassword")
		shareeMobileNumber = request.POST.get("shareeMobileNumber")
		shareeBirthdate = request.POST.get("shareeBirthdate")
		
		obj = Sharee(email = shareeEmail, firstname = shareeFirstName, lastname = shareeLastName, password = shareePassword, contactnumber = shareeMobileNumber, birthday = shareeBirthdate)
		obj.save()
		return redirect('registers:gorent_loginSharee_view')

class GoRentLandingPage(View):
	def get(self, request):
		return render(request, 'registers/landingPage.html') # THIS REFERES TO TEMPLATE PATH, FIND url.py  IF YOU WANT TO LIVE ACCESS THE PAGE 
		