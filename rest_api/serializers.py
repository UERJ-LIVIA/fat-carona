from accounts.models import Profile
from Rides.models import Ride
from django.contrib.auth.models import User
from rest_framework import serializers


class CarregaDadosPassageirosSerializer(serializers.ModelSerializer):
    class Meta:
        nome_usuario = serializers.SerializerMethodField()
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email']

        def get_nome_usuario(self, obj):
            return obj.nome.username


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['diretorio', 'user', 'email', 'senha', 'cnh', 'placa_carro']


class RidesSerializer(serializers.ModelSerializer):
    passageiros = CarregaDadosPassageirosSerializer(many=True)

    class Meta:
        model = Ride
        fields = ['modalidade', 'motorista', 'passageiros',
                  'data_publicaçao', 'data_saida', 'info']

    def get_nome_passageiro(self, obj):
        return obj.nome.passageiros
