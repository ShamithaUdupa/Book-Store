from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Book,Shopping_Cart,Selling_Cart
# Create your views here.

def login(request):
	return render(request,'login.html')
	
def user(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		result=User.objects.filter(username=username,password=password).count()
		if result==1 :
			request.session['username']=username
			return render(request,'user.html')
		elif result==0 :
			return render(request,'login.html')
	elif request.method == 'GET':
		query=request.GET.get('query')
		result=Book.objects.filter(title=query)
		return render(request,'user.html',{'context':result})

def register(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		email=request.POST.get('email')
		obj=User.objects.create(username=username,password=password,email=email)
		return render(request,'login.html')
		
def shoppingcart(request):
	if request.method == 'GET':
		var=request.GET.get('action','')
		if(var=="add"):
			p1=Shopping_Cart(isbn=request.GET.get('isbn'),title=request.GET.get('title'),author=request.GET.get('author'),price=request.GET.get('price'))
			p1.save()
		elif(var=="remove"):
			Shopping_Cart.objects.filter(isbn=request.GET.get('isbn')).delete()
		obj=Shopping_Cart.objects.all()
		return render(request,'shoppingcart.html',{'context':obj})
	
def sellingcart(request):
	if request.method == 'GET':
		var=request.GET.get('action','')
		if(var=="add"):
			p1=Selling_Cart(isbn=request.GET.get('isbn'),title=request.GET.get('title'),author=request.GET.get('author'),price=request.GET.get('price'))
			p1.save()
		elif(var=="remove"):
			p2=Selling_Cart.objects.filter(isbn=request.GET.get('isbn'))
			p2.delete()
		obj=Selling_Cart.objects.all()
		return render(request,'sellingcart.html',{'context':obj})
	
def logout(request):
	del request.session['username']
	return render(request,'login.html')
