function register(){
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://localhost:8000/register', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    

	var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;
    var age = document.getElementById("age").value;

	var body = "login=" + login + "&password=" + password + "&age="+age;
	xhr.send(body); 
}

function login(){
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://localhost:8000/login', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    

	var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;

	var body = "login=" + login + "&password=" + password + "&age="+age;
	xhr.send(body); 
}