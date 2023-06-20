from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.views import APIView

from ..models import Example
from .serializers import RideAPISerializer


# CONVERTED FUNCTION-BASED VIEW TO CLASS-BASED /
# REFERENCE: https://www.django-rest-framework.org/tutorial/3-class-based-views/

# FOR STATUS CODES, CHECK OUT: https://www.django-rest-framework.org/api-guide/status-codes/

class RideAPIView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):

    queryset = Example.objects.all()
    serializer_class = RideAPISerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        queryset = Example.objects.all()

        # return self.create(request, *args, **kwargs)

        serializer_class = RideAPISerializer(queryset, many=True)
        if serializer_class.is_valid():
            serializer_class.save()
            # response_msg = {'msg': 'TEST - SUCCESS'}
            # return Response(response_msg)
            return Response(serializer_class.data)
        else:
            # return Response({'msg': serializer_class.errors})
            return Response(serializer_class.errors, status=status.HTTP_404_NOT_FOUND)
