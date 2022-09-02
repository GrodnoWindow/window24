from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.middleware import csrf
from core import settings
from .serializers import LoginSerializer, LogoutSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        response = Response()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            tokens = serializer.data["tokens"]
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=tokens["access"],
                # expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = serializer.data
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = Response()
        response.delete_cookie(key='access_token')
        response.delete_cookie(key='csrftoken')

        serializer.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)
