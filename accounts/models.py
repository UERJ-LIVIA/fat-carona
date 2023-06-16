from django.db import models

# Create your models here.
from django.db import models as mo
from django.contrib.auth.models import User

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