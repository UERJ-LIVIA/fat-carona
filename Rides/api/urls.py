from django.urls import path
from .views import (RidesAPIView,
                    RideDetailAPIView,
                    ProfileDetailAPIView,
                    ProfilesAPIView,
                    )


# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride'),
    path('rides/<int:pk>/profiles',
         ProfilesAPIView.as_view(), name='curso_profiles'),
    path('rides/<int:pk>/profiles/',
         ProfileDetailAPIView.as_view(), name='curso_profiles'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles')

]
