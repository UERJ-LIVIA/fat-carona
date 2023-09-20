from django.urls import path
from .views import (RidesAPIView,
                    RideAPIView,
                    ProfileAPIView,
                    ProfilesAPIView,
                    RidesFiltroAPIView, 
                    )


# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/rides-filtro', RidesFiltroAPIView.as_view(), name='rides_filtro'),
    path('rides/<int:pk>/', RideAPIView.as_view(), name='ride'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles'),
    path('rides/<int:ride_pk>/profiles/<int:profile_pk>',
         ProfileAPIView.as_view(), name='curso_profiles')
]
