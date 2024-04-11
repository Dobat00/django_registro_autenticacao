from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import CadastroForm, LoginForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import auth
# Create your views here.

def home(request):
    form = LoginForm()
    context = {
        "form":form,
    }
    if (request.method == "POST"):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return  redirect('logado')
    return  render(request,'home.html', context) 

def cadastro(request):
    form = CadastroForm()
    context = {
        "form":form
    }
    if (request.method == "POST"):
        form = CadastroForm(request.POST);
        if (form.is_valid()):
            form.save()
            return redirect('home')
    return render(request, 'cadastro.html', context)

def logado(request):
    return HttpResponse('logado')
