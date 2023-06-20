from rest_framework import serializers

from ..models import Example


class RideAPISerializer(serializers.ModelSerializer):

    date_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Example
        fields = '__all__'

    def date_format(self, obj):
        # Input for date must be standardized...
        # Return assumes 'date' is a DateTimeField for model
        # From model (WIP), pub_date = models.DateTimeField(default=datetime.datetime.now)
        return obj.date.strftime("%Y-%m-%d %H:%M:%S")