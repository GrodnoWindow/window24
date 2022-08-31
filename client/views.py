from django.forms import model_to_dict
from django.shortcuts import render

from users.serializers import UserSerializer
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    def get(self,request, **kwargs):
        pk = kwargs.get('pk', None)
        w = Client.objects.get(pk=pk)
        return Response({"clients": ClientSerializer(w).data})


    # def post(self,request):
    #     serializer = ClientSerializer(data=request.data) # validator to json
    #     serializer.is_valid(raise_exception=True)
    #     # serializer_user = UserSerializer(request.user) # current user
    #     # current_user = serializer_user.data['username']
    #     serializer.save()
    #     return Response({'client': serializer.data})


    def put(self,request, *args,**kwargs):
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


# class ClientAPIView(APIView):
#     def get(self, request):
#         lst = Client.objects.all().values()
#         return Response({'name':list(lst)})
