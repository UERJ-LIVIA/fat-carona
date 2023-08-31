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
    
    # DRF
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action

from accounts.models import Profile
from Rides.models import Rides
from .serializers import RidesSerializer, ProfileSerializer

"""
API de Caronas (v1)
"""


class RidesAPIView(generics.ListCreateAPIView):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer

    def get_queryset(self):
        if self.kwargs.get('rides_pk'):
            return self.queryset.filter(rides_id=self.kwargs.get('rides_pk'), ordering=id[-1])
        return self.queryset.all()


class RideAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer

    lookup_field = 'pk'


"""
API de Perfis (v1)
"""


class ProfilesAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    lookup_field = 'pk'

    def get_object(self):
        if self.kwargs.get('rides_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('rides_pk'),
                                     pk=self.kwargs.get('profile_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('profile_pk'))


"""
API (v2)
"""


class RideViewSet(viewsets.ModelViewSet):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer
    permission_class = permissions.DjangoModelPermissions

    @action(detail=True, methods=['get'])
    def profiles(self, request, pk=None):
        self.pagination_class_sizes = 1
        profiles = Profile.objects.all()
        page = self.paginate_queryset(profiles)

        if page is not None:
            serializer = ProfileSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
