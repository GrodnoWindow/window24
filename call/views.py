from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializer import CallSerializer
from .models import Call
from .serializer import CallSerializer
from rest_framework import generics, viewsets, mixins
from .utils import parse_active_call

class CallViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet): # get, post , get<id>, put<id>, path<id>

    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def get_queryset(self, *args, **kwargs):
        parse_active_call()
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


