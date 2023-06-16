from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth, logout
from django.http import HttpResponseRedirect

# Create your views here.


def cadastro(request):
    if request.method == 'POST':
            try: # verificar se usuario ja existe!
                 user= User.objects.get (request.POST['username'])
            except: # se nao existir usuario, cria usuario puxando dados inseridos no frontend !
                 user=User.obejects.create_user(request.POST['username'],password=request.POST['senha'],email=request.POST['email'])    
                 auth.login(request,user)

    return  HttpResponseRedirect(request.META.get('login.html'))

