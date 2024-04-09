from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request, 'myapp/index.html') 

def register(request):
    form = CreateUserForm()

    if (request.method =='POST'):
        form = CreateUserForm(request.POST);

        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {"registerform":form}
    return render(request, 'myapp/register.html', context) 

def my_login(request):
    form = LoginForm()
    if (request.method =="POST"):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.
    return render(request, 'myapp/my-login.html') 

def dashboard(request):
    return render(request, 'myapp/dashboard.html') 
