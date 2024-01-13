from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Festival
from .serializers import FestivalSerializer
from django.http import Http404
from rest_framework import status

class FestivalList(APIView):
    def get(self, request):
        festivals = Festival.objects.all()
        serializer = FestivalSerializer(festivals, many=True)
        return Response(serializer.data)


    def post(self, request):
            serializer = FestivalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class FestivalDetail(APIView):
    def get_object(self, pk):
        try:
            return Festival.objects.get(pk=pk)
        except Festival.DoesNotExist:
                raise Http404
    def get(self, request, pk):
        festival = self.get_object(pk)
        serializer = FestivalSerializer(festival)
        return Response(serializer.data)
