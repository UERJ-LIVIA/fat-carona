from django.urls import path

from .views import (
    exampleAPIView,
)

urlpatterns = [
    path('example/', exampleAPIView.as_view()),
]