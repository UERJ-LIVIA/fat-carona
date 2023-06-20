from django.urls import path
from rides.api.views import RideAPIView

urlpatterns = [
    path('rides/', RideAPIView.as_view()),
]