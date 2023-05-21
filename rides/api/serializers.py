from rest_framework import serializers

from ..models import Example

class ExampleSerializer(serializers.ModelSerializer):
    """
    Utilizado em: exampleAPIView
    """

    class Meta:
        model = Example
        fields = ('__all__')