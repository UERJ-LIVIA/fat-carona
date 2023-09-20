from django.urls import path
from .views import (RidesAPIView,
                    RideDetailAPIView,
                    ProfileDetailAPIView,
                    ProfilesAPIView,
                    RidesFiltroAPIView,
                    )


# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/rides-filtro', RidesFiltroAPIView.as_view(), name='rides_filtro'),
    path('rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride'),
    path('rides/<int:pk>/profiles',
         ProfilesAPIView.as_view(), name='curso_profiles'),
    path('rides/<int:pk>/profiles/',
         ProfileDetailAPIView.as_view(), name='curso_profiles'),
    path('profiles/<int:profile_pk>', ProfilesAPIView.as_view(), name='profiles'),

]
