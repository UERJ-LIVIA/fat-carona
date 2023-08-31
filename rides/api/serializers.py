from rest_framework import serializers

from ..models import Example

class ExampleSerializer(serializers.ModelSerializer):
    """
    Utilizado em: exampleAPIView
    """

    class Meta:
        model = Example
        fields = ('__all__')

from accounts.models import Profile
from rest_framework import serializers
from Rides.models import Rides


class RidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rides
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
