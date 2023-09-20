# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action


from accounts.models import Profile
from rides.models import Ride
from .serializers import RidesSerializer, ProfileSerializer
from django.contrib.auth.models import User
"""
API de Rides (v1)
"""


class RidesAPIView(generics.ListCreateAPIView):
    """
    Listar Rides mediante filtro
    Ref POST :
    {
    "modalidade": "DEFAULT",
    "motorista": 7,
    "data_saida": "2023-09-20T14:45:00Z",
    "info": "Teste"
}

    """
    queryset = Ride.objects.all()
    serializer_class = RidesSerializer

    # listar Rides  -> request GET

    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        return self.queryset.filter(**dicionario_request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RideDetailAPIView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin
                        ):

    queryset = Ride.objects.all()
    serializer_class = RidesSerializer

    lookup_field = 'pk'

    def delete(self, request, *args, **Kwargs):
        return self.destroy(request, *args, **Kwargs)

    def get(self, request, *args, **Kwargs):
        return self.retrieve(request, *args, **Kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


"""
API de Perfis (v1)

"""


class ProfilesAPIView(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileDetailAPIView(
        generics.GenericAPIView,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **Kwargs):
        return self.destroy(request, *args, **Kwargs)


"""
API (v2)
"""


class RidesViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RidesSerializer
    permission_class = permissions.DjangoModelPermissions

    @action(detail=True, methods=['get'])
    def profiles(self, request, pk=None):
        self.pagination_class_sizes = 5
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
