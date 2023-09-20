from django.urls import path
from .views import (RidesAPIView,
                    RidDetailAPIView,
                    ProfileDetailAPIView,
                    ProfilesAPIView,
                    RidesFiltroAPIView,
                    )


# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/rides-filtro', RidesFiltroAPIView.as_view(), name='rides_filtro'),
    path('rides/<int:pk>/', RidDetailAPIView.as_view(), name='ride'),
    path('rides/<int:ride_pk>/profiles',  ProfilesAPIView.as_view(), name='curso_profiles'),
    path('rides/<int:ride_pk>/profiles/<int:profile_pk>',
         ProfileDetailAPIView.as_view(), name='curso_profiles'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles'),
    
]
