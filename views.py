from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from CaronaFat.models import Profile, User
from .forms import PerfilForm


# Create your views here.


def cadastro(request):
    Profile.objects.get(user=request.user,
                        nome=request.user, email=request.user)

    client = Profile.objects.get(user='user', nome='nome', email='email')
    client.user = 'user'
    client.nome = 'nome'
    client.email = 'email'
    client.save()


def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        password = request.POST['password']
        user = authenticate(request, username=nome, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            error_message = 'Informações incorretas. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})


def logout(request):
    logout(request)
    return render(request, 'login.html')


def check_perfil(request):
    try:
        perfil = Profile.objects.get(usuario=request.user)
        if request.method == 'POST':
            form = PerfilForm(request.POST, instance=perfil)
            if form.is_valid():
                form.save()
                return redirect('pagina_inicial')
        else:
            form = PerfilForm(instance=perfil)
        return render(request, 'cadastro.html', {'form': form})
    except Profile.DoesNotExist:
        return redirect('cadastro.html')
