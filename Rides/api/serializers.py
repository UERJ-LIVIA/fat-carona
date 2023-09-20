from accounts.models import Profile
from rides.models import Ride
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
        fields = '__all__'


class RidesSerializer(serializers.ModelSerializer):
    passageiros = CarregaDadosPassageirosSerializer(many=True, required=False)
    passageiros_id = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(),
                                                        source='passageiros')

    class Meta:
        model = Ride
        fields = ['id', 'motorista', 'data_publicaçao',
                  'data_saida', 'info', 'modalidade', 'passageiros', 'passageiros_id']

    def update(self, instance, validated_data):
        passageiros = validated_data.pop('passageiros')
        instance = super(RidesSerializer, self).update(
            instance, validated_data)
        instance.passageiros.clear()
        for passageiro in passageiros:
            instance.passageiros.add(passageiro)
            return instance

    def get_nome_passageiros(self, obj):
        return obj.nome.passageiros
