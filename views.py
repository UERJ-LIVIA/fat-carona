from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from CaronaFat.models import Profile,User

# Create your views here.


def cadastro(request):
    Profile.objects.get(user=request.user,nome=request.user,email=request.user)

    client = Profile.objects.get(user='user',nome='nome',email='email')
    client.user='user'
    client.nome='nome'
    client.email='email'
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
    return render(request,'login.html')
   



