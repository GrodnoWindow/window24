from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .serializer import CallSerializer
from config.pagination import CustomPagination
from .models import Call
from .serializer import CallSerializer
from rest_framework import generics, viewsets, mixins
from client.models import Client


class CallGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    queryset = Call.objects.all().values().order_by('-datetime')
    serializer_class = CallSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})

        return self.list(request)


class CallAPIView(generics.ListAPIView):  # all requests get,put,patch ...
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        w = Call.objects.get(pk=pk)
        return Response({"data": CallSerializer(w).data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PATCH not allowed'})

        try:
            instance = Call.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = CallSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})
