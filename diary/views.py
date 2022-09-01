from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializer import TaskSerializer
from .models import Task

class TaskAPIList(generics.ListCreateAPIView): # GET and POST requests
    queryset = Task.objects.filter(overdue=False).values()
    serializer_class = TaskSerializer

    # def get(self,request, **kwargs):
    #     is_overdue = kwargs.get('slug', None)
    #     w = Task.objects.filter(overdue=is_overdue)
    #     return Response({"Tasks": TaskSerializer(w,many=True).data})

