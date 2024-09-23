from django.shortcuts import render
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserSerializer

# Create your views here.
class LoginView(views.APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message":'로그인 성공',"data":serializer.validated_data}, status=status.HTTP_200_OK)
        return Response({"message":'로그인 실패',"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    serializer = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":'회원가입 성공',"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message":'회원가입 실패',"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    