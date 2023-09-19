from django.db import models as mo
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.


class Profile(mo.Model):
    class Genero(mo.TextChoices):
        M = 'M', _('Masculino')
        F = 'F', _('Feminino')

    class Tipos(mo.TextChoices):
        PASSAGEIRO = 'PASSAGEIRO', _('Passageiro')
        MOTORISTA = 'MOTORISTA', _('Motorista')

    user = mo.ForeignKey(User, on_delete=mo.CASCADE)
    nome = mo.CharField(max_length=20)
    email = mo.EmailField(max_length=50)
    placa_carro = mo.CharField(max_length=8, null=True, blank=True)
    cnh = mo.IntegerField(blank=True, null=True)
    diretorio = mo. ImageField(upload_to=None, height_field=None,
                               width_field=None,  blank=False,
                               default='/templates/static/logo_uerj1.jpg')
    senha = mo.CharField(max_length=50, default='*********')
    # gender = mo.CharField(
    #     max_length=12, choices=Genero.choices, default='Genero.M')
    # tipos = mo.CharField(max_length=12, choices=Tipos.choices,
    #                      default='Tipos.Passageiro')
    # matricula = mo.IntegerField()
    # idade = mo.IntegerField()
