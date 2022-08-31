from django.forms import model_to_dict
from django.shortcuts import render

from users.serializers import UserSerializer
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView



class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    def get(self,request):
        w = Client.objects.all()
        return Response({"clients": ClientSerializer(w,many=True).data})


    def post(self,request):
        serializer = ClientSerializer(data=request.data) # validator to json
        serializer.is_valid(raise_exception=True)

        serializer_user = UserSerializer(request.user) # current user
        current_user = serializer_user.data['email']
        serializer.save()

        # client_new = Client.objects.create(
        #     author = current_user,
        #     name = request.data['name'],
        # )

        return Response({'client': serializer.data})


# class ClientAPIView(APIView):
#     def get(self, request):
#         lst = Client.objects.all().values()
#         return Response({'name':list(lst)})

