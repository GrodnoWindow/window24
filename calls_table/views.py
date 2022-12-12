
from rest_framework.response import Response

from config.pagination import CustomPagination
from .models import *
from rest_framework import generics, viewsets, mixins
from .serializer import *


class CallsTableGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    queryset = CallsTable.objects.all()
    serializer_class = CallsTableSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({'data': self.retrieve(request, pk).data})

        return self.list(request)


class CallsTableAPIView(generics.ListAPIView):  # all requests get,put,patch ...
    queryset = CallsTable.objects.all()
    serializer_class = CallsTableSerializer

    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        w = CallsTable.objects.get(pk=pk)
        return Response({"data": CallsTableSerializer(w).data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = CallsTable.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = CallsTableSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})
