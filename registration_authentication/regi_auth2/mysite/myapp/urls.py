from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logado', views.logado, name = 'logado')
]
