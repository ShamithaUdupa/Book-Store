from django.db import models
# Create your models here.

class User(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	email=models.EmailField(max_length=70,unique=True)
	
	def __str__(self):
		return self.username

class Book(models.Model):
	title=models.CharField(max_length=50)
	isbn=models.IntegerField()
	author=models.CharField(max_length=25)
	price=models.DecimalField(max_digits=7,decimal_places=2)
	quantity=models.IntegerField()
	
	def __str__(self):
		return self.title
		
class Shopping_Cart(models.Model):
	title=models.CharField(max_length=50)
	isbn=models.IntegerField()
	author=models.CharField(max_length=25)
	price=models.DecimalField(max_digits=7,decimal_places=2)
	
	def __str__(self):
		return self.title
