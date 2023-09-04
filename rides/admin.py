from django.contrib import admin
from .models import Rides, Profile

# Register your models here.


@admin.register(Rides)
class RidesAdmin(admin.ModelAdmin):
    list_display = ('motorista','data_publicaçao', 'data_saida', 'info')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'idade', 'email', 'matricula', 'gender')
