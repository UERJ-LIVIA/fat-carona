from rest_framework.response import Response
from rest_framework import generics, mixins

from ..models import Example
from .serializers import ExampleSerializer


class exampleAPIView(generics.GenericAPIView, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Convert date to proper format first or nah????
        departure_date = request.data.get('departure_date')

        # If additional info is inputted by the user, it can be requested from here
        additional_info = request.data.get('additional_info')
        user = request.data.get('user')

        # Create ride as a dictionary with the input user as the driver
        ride_data = {
            'departure_date': departure_date,
            'additional_info': additional_info,
            'driver': user
        }

        # https://www.django-rest-framework.org/api-guide/generic-views/#examples
        # https://www.django-rest-framework.org/api-guide/serializers/
        # https://www.django-rest-framework.org/api-guide/status-codes/
        #
        #   serializer = self.get_serializer(data=ride_data)
        #   self.perform_create(serializer)
        #
        #   return Response(serializer.data, status=status.HTTP_201_CREATED)

        return self.create(request, *args, **kwargs)