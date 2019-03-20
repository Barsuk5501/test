from django.db import models
import django

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
class Admin(MyUser):
	IsAdmin = models.BooleanField(default = True)
	def registerAdmin(self,login,password,age):
		admin = Admin(login = "123",password = "123",age = 123,IsAdmin = True)
		admin.save()
class Post(models.Model):

	name = models.CharField(max_length=100)
	text = models.CharField(max_length=800)
	date = models.DateField(default =django.utils.timezone.now)
	user = models.ForeignKey(MyUser,on_delete=models.CASCADE)



