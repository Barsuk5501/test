from django.db import models

class MyUser(models.Model):
	login = models.CharField(max_length=80)
	password = models.CharField(max_length=20)
	age = models.IntegerField()
	
	def registerUser(self,login,password,age):
		MyUser.objects.create(
			login =login,
 	        password=password,
			age=age
		)

