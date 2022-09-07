from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response

from .serializer import CallSerializer
from .models import Call
from .serializer import CallSerializer
from rest_framework import generics, viewsets
import time


# class CallAPIList(generics.ListCreateAPIView): # GET and POST requests
#     queryset = Call.objects.all()
#     serializer_class = CallSerializer

    # def get(self, request, *args, **kwargs):
    #
    #     # return self.list(request, *args, **kwargs)


class CallViewSet(viewsets.ModelViewSet): # get, post , get<id>, put<id>, path<id>
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = Call.objects.all()
        return queryset

# class CallAPIView(generics.ListAPIView): # all requests get,put,patch ...
#     queryset = Call.objects.all()
#     serializer_class = CallSerializer
#
#     def get(self,request, **kwargs):
#         pk = kwargs.get('pk', None)
#         w = Call.objects.get(pk=pk)
#         return Response({"clients": CallSerializer(w).data})
#


