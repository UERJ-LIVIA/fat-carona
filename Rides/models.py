from django.db import models as mo
from datetime import datetime
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.


class Ride(mo.Model):
    class Modalidade(mo.TextChoices):
        DEFAULT = 'DEFAULT', _('Padrão')
        UBER = 'UBER', _('Uber')

    motorista = mo.ForeignKey(
        User, on_delete=mo.CASCADE, related_name='driver', blank=True, null=True)
    passageiro = mo.ManyToManyField(User, related_name='passenger', null=True)
    data_publicaçao = mo.DateTimeField(default=datetime.now)
    data_saida = mo.DateTimeField(default=datetime.now)
    info = mo.TextField(max_length=200, blank=True)
    modalidade = mo.CharField(max_length=12, choices=Modalidade.choices,
                              default='Modalidade.DEFAULT')
