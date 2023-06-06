from django.db import models as mo
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Profile(mo.Model):
    class Genero(mo.TextChoices):
        Opcao_1 = 'Masculino'
        Opcao_2 = 'Feminino'

    user = mo.OneToOneField(User, on_delete=mo.CASCADE)
    nome = mo.CharField(max_length=20)
    idade = mo.IntegerField(max_length=3)
    email = mo.EmailField(max_length=50)
    matricula = mo.IntegerField(max_length=20)
    gender = mo.CharField(
        max_length=12, choices=Genero.choices, default='Opcao_1')


class Rides(mo.Model):
    User = mo.ForeignKey(User, on_delete=mo.CASCADE)
    motorista = mo.CharField(max_length=50)
    passageiro = mo.CharField(max_length=50)
    data_publicaçao = mo.DateTimeField(datetime.datetime.now)
    saida = mo.DateTimeField(default=datetime.datetime.now)
    info = mo.TextField(max_length=200, blank=True)
