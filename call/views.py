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
from .utils import *


class CallView(APIView):

    queryset = Call.objects.all()
    serializer_class = CallSerializer
    pagination_class = CustomPagination

    def get(self, request):
        # database_reader() # CSV FILE
        if parse_active_calls():
            data = Call.objects.all().values().order_by('-id')[:1]
        else:
            data = []
        return Response({
            'calls': list(data)
        })

    # def get(self, request, pk=None):
    #     if pk:
    #         return Response({
    #             'data': self.retrieve(request, pk).data
    #         })
    #
    #     return self.list(request)


class CallGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):

    queryset = Call.objects.all().values().order_by('-datetime')
    serializer_class = CallSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'calls': self.retrieve(request, pk).data
            })

        return self.list(request)

class CallAPIView(generics.ListAPIView): # all requests get,put,patch ...
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def get(self,request, **kwargs):
        pk = kwargs.get('pk', None)
        w = Call.objects.get(pk=pk)
        return Response({"clients": CallSerializer(w).data})

    def patch(self,request, *args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})

        try:
            instance = Call.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not exists'})

        serializer = CallSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data})

        # client_new = Client.objects.create(
        #     author = current_user,
        #     name = request.data['name'],
        # )


