from django.shortcuts import render
from . models import MyUser
from . models import Post
from django.http import HttpResponse

def register (request):	
	print("іваіваіва")
	if request.method == "POST": 
		body = request.body.decode('utf-8')
		body = body.split("&")

		password = body[0].split("=")[1]
		login = body[1].split("=")[1]
		age = body[2].split("=")[1]

		user = MyUser()
		user.registerUser(login,password,age)

		response = HttpResponse("Пользователь был добавлен")
		return response

	elif request.method == "GET":
	    return render(request, 'app/register.html', {})

def login (request):
	if request.method == "POST": 
		body = request.body.decode('utf-8')
		body = body.split("&")

		password = body[1].split("=")[1]
		login = body[0].split("=")[1]
		
		users = MyUser.objects.filter(login = login, password = password)
		
		if len(users) > 0:
			response = HttpResponse("Пользователь был найден")
		else:
			response = HttpResponse("Пользователь не был найден")	
		return response

	elif request.method == "GET":
	    return render(request, 'app/login.html', {})

def news(request):
	posts = Post.objects.filter()
	return render(request, 'app/news.html', {'posts': posts})


