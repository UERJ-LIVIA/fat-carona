from django.db import models

import datetime

# Create your models here.
from django.db import models as mo
import datetime
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.


class Rides(mo.Model):
    Profile = mo.ForeignKey(User, on_delete=mo.CASCADE)
    motorista = mo.ForeignKey(User,on_delete=mo.CASCADE,related_name='driver')
    passageiro = mo.ManyToManyField(User,related_name='passenger')
    data_publicaçao = mo.DateTimeField(datetime.datetime.now)
    saida = mo.DateTimeField(default=datetime.datetime.now)
    info = mo.TextField(max_length=200, blank=True)
