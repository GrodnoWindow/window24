from django.forms import model_to_dict
from django.shortcuts import render

from users.serializers import UserSerializer
from .models import Client
from .serializer import ClientSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class ClientAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):

        serializer_user = UserSerializer(request.user) # current user
        current_user = serializer_user.data['username']

        client_new = Client.objects.create(
            author=current_user,
            number=request.data['number'],
            name=request.data['name'],
        )

        return Response({'client': ClientSerializer(client_new).data})


class ClientAPIView(generics.ListAPIView): # all requests get,put,patch ...
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self,request, **kwargs):
        pk = kwargs.get('pk', None)
        w = Client.objects.get(pk=pk)
        return Response({"clients": ClientSerializer(w).data})

    def patch(self,request, *args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})

        try:
            instance = Client.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not exists'})

        serializer = ClientSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data})

        # client_new = Client.objects.create(
        #     author = current_user,
        #     name = request.data['name'],
        # )
