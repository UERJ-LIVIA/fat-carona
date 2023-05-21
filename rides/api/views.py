from rest_framework.response import Response
from rest_framework import generics, mixins

from ..models import Example
from .serializers import ExampleSerializer

class exampleAPIView(generics.GenericAPIView, 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    """
    Endpoint de exemplo.
    """
    queryset            = Example.objects.all()
    serializer_class    = ExampleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)