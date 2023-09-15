# DRF
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action


from accounts.models import Profile
from Rides.models import Ride
from .serializers import RidesSerializer, ProfileSerializer, CarregaDadosPassageirosSerializer
from django.contrib.auth.models import User
"""
API de Rides (v1)
"""


class RidesAPIView(generics.ListCreateAPIView):
    """
    Listar Rides mediante filtro
    """
    queryset = Ride.objects.all()
    serializer_class = RidesSerializer

    # listar Rides  -> request GET

    def get_queryset(self):
        dicionario_request = self.request.GET.dict()
        print(dicionario_request)
        return self.queryset.filter(**dicionario_request)

    def post(self, request):
        serializer = RidesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.create(request, serializer.data, status=status.HTTP_201_CREATED)


class RideAPIView(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin
                  ):

    queryset = Ride.objects.all()
    serializer_class = RidesSerializer

    lookup_field = 'pk'

    def delete(self, request, *args, **Kwargs):
        return self.destroy(request, *args, **Kwargs)

    def get(self, request, *args, **Kwargs):
        return self.retrieve(request, *args, **Kwargs)


# metodo para filtrar caronas segundo usuario como passageiro
class RidesFiltroAPIView(generics.ListAPIView):
    queryset = Ride.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        lista_filtro = self.request.GET.dict()
        return Profile.objects.filter(**lista_filtro).all()


"""
API de Perfis (v1)

"""


class ProfilesAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostProfileAPIView(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         ):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        new_profile = Profile.objects.create(
            nome=data['nome'],
            email=data['email'],
            senha=data['senha'],
            placa_carro=data['placa_carro'],
            cnh=data['cnh'],
            diretorio=data['diretorio'],
            user=User.objects.get(pk=data['user'])
        )
        serializer = ProfileSerializer(new_profile, many=False)
        return Response(serializer.data, new_profile)


class DeleteProfileAPIView(generics.GenericAPIView,
                           mixins.DestroyModelMixin,
                           mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        data = Profile.objects.all(pk='profile_pk')
        profile_created = Profile.objects.delete(data)
        serializer = ProfileSerializer(data, many=False)
        return Response(serializer.data, profile_created)


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    lookup_field = 'pk'

    def get_object(self):
        if self.kwargs.get('Rides_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('Rides_pk'),
                                     pk=self.kwargs.get('profile_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('profile_pk'))


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


"""
# Customizando as ViewSets de Profiles usando mixins!
class ProfileViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Profile.objects.all()
    serialiazer_class = ProfileSerializer

"""
