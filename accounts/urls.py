from django.urls import path
from . import views

# create your app routes here!

urlpatterns= [
    path('login/',views.login,name='login'),
    path('deslogar/',views.deslogar,name='logout'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('atualizar_perfil/',views.atualizar_perfil,name='atualizar_perfil')
]