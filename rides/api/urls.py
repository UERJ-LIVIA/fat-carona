from django.urls import path

from .views import (
    exampleAPIView,
)

urlpatterns = [
    path('example/', exampleAPIView.as_view()),
]

from django.urls import path
from rest_api.views import( RidesAPIView,
                            ProfileAPIView,
                            ProfilesAPIView,
                            RideAPIView,
                            RideViewSet,
                            ProfileViewSet
                           )
#DRF
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('rides',RideViewSet)
router.register('profiles',ProfileViewSet)

# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/<int:pk>/', RideAPIView.as_view(), name='ride'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileAPIView.as_view(), name='profile')
]
