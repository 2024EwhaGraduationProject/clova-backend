from django.shortcuts import render, get_object_or_404
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Lost
from .serializers import LostSerializer, LostlistSerializer

# Create your views here.
class LostlistView(views.APIView):
    def get(self, request, *args, **kwargs):
        lostitems = Lost.objects.all()
        serializer = LostlistSerializer(lostitems, many=True)

        return Response({'message': 'lostitem get 성공', 'data': serializer.data})

class LostDetailView(views.APIView):
    def get(self, request, lostid):
        lost = get_object_or_404(Lost, id=lostid)
        serializer = LostSerializer(lost)

        return Response({'message': 'lostdetail get 성공', 'data': serializer.data})