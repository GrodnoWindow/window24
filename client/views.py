from django.forms import model_to_dict
from django.shortcuts import render
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView



class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    def get(self,request):
        lst = Client.objects.all().values()
        return Response({"clients": list(lst)})


    def post(self,request):
        client_new = Client.objects.create(
            name = request.data['name']
        )

        return Response({'client': model_to_dict(client_new)})

# class ClientAPIView(APIView):
#     def get(self, request):
#         lst = Client.objects.all().values()
#         return Response({'name':list(lst)})

