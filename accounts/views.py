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


def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        password = request.POST['password']
        user = auth(request, username=nome, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            error_message = 'Informações incorretas. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
        

def deslogar(request):
    logout(request)
    return render(request, 'login.html')
