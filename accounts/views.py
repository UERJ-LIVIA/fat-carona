from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
            return  HttpResponseRedirect(request.META.get('login.html'))
        

def deslogar(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('login.html'))


  
  
  
## @login_required
def atualizar_perfil(request):
     if request.method == 'POST':
        # Verifica se o usuário possui um perfil
        try:
            perfil = request.user.perfil
        except perfil.DoesNotExist:
            perfil = None

        # Atualiza o perfil ou cria um novo
        if perfil:
            # Atualiza o perfil com base nos dados repassados
            redirect(request,'atualizar_perfil.html')
            perfil.campo1 = request.POST.get('campo1')
            perfil.campo2 = request.POST.get('campo2')
            perfil.save()
         
        else:
            # Cria um novo perfil
            redirect(request,'cadastro.html')
            perfil = perfil.objects.create(
                usuario=request.user,
                campo1=request.POST.get('campo1'),
                campo2=request.POST.get('campo2'),
               )
            

        # Redireciona o usuário para a mesma página
        return HttpResponseRedirect(request.META.get('login.html'))