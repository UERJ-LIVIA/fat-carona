from django.urls import path
from .views import (RidesAPIView,
                    RideAPIView,
                    ProfileAPIView,
                    ProfilesAPIView,
                    PostProfileAPIView,
                    DeleteProfileAPIView,
                    RidesFiltroAPIView,
                    RidesViewSet,
                    ProfileViewSet
                    )
# DRF
"""
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('rides', RidesViewSet)
router.register('profiles', ProfileViewSet)

"""


# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/rides-filtro', RidesFiltroAPIView.as_view(), name='rides_filtro'),
    path('rides/<int:pk>/', RideAPIView.as_view(), name='ride'),
    path('rides/<int:ride_pk>/profiles',
         ProfilesAPIView.as_view(), name='curso_profiles'),
    path('rides/<int:ride_pk>/profiles/<int:profile_pk>',
         ProfileAPIView.as_view(), name='curso_profiles'),
    path('profiles/post', PostProfileAPIView.as_view(), name='profiles_post'),
    path('profiles/<int:pk>/del/',
         DeleteProfileAPIView.as_view(), name='profiles_del'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileAPIView.as_view(), name='profile')
]
