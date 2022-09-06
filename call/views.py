from django.forms import model_to_dict
from django.shortcuts import render

from .serializer import CallSerializer
from .models import Call
from .serializer import CallSerializer
from rest_framework import generics


class CallAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    # def get(self, request, *args, **kwargs):
    #
    #     # return self.list(request, *args, **kwargs)
