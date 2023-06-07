from django.urls import path
from . import views

# create your app routes here!

urlpatterns= [
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('cadastro/',views.cadastro,name='cadastro')
]