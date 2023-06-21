from django.db import models as mo
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.


class Profile(mo.Model):
    class Genero(mo.TextChoices):
     M = 'M', _('Masculino')
     F = 'F', _('Feminino')

    user = mo.OneToOneField(User, on_delete=mo.CASCADE)
    nome = mo.CharField(max_length=20)
    idade = mo.IntegerField(max_length=3)
    email = mo.EmailField(max_length=50)
    matricula = mo.IntegerField(max_length=20)
    gender = mo.CharField(
        max_length=12, choices=Genero.choices, default='Genero.M')