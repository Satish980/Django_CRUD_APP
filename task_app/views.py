from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails
from django.contrib.auth.models import auth
from .forms import UserForm
# Create your views here.


def index(request):
	err = ""
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		data = UserDetails.objects.get(email = email)
		print(data,data.password,data.email)
		if data.email == email and data.password == password:
			return redirect('/data/')
		elif data.email == email and data.password != password:
			err = "Invalid Credentials"
			return render(request,"index.html",{"error":err})


	return render(request,"index.html")


def data(response):
	ls = UserDetails.objects.all()
	return render(response, "userdetail.html",{"ls":ls})

def signup(request):
	if request.method == "POST":
		username = request.POST['uname']
		email = request.POST['email']
		password = request.POST['password']
		address = request.POST['address']
		print(username," ",email," ",password," ",address)
		#user = UserDetails.objects.creat_user()
		#user.save()
		user = UserDetails(username = username, email = email, password = password, address = address)
		user.save()
		print('User Created')
		return redirect('/')
	return render(request, "signup.html")

def update(request,id=0):
	if request.method == "GET":
		#print(id)
		data = UserDetails.objects.filter(id=id).first()
		form = UserForm(instance = data)
		return render(request, "update.html",{"form" : form})
	else:
		try:
			data = UserDetails.objects.filter(id=id).first()
			#data = UserDetails.objects.get(email = email)
			form = UserForm(request.POST, instance=data)
			if form.is_valid():
				form.save()
		except Exception as e:
			return HttpResponse(str(e)) 
	
	return redirect('/data/')


def delete(request,id=0):
	print(id)
	try:
		data = UserDetails.objects.get(id=id)
		print(data)
		data.delete()
		return redirect('/data/')
	except Exception as e:
		return HttpResponse(str(e)) 

def logout(request):
	auth.logout(request)
	return redirect('/')
