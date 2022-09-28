from .models import Constructor
from .serializer import ConstructorSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, mixins
from rest_framework.response import Response
from config.pagination import CustomPagination


class ConstructorGenericAPIList(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'calls': self.retrieve(request, pk).data
            })

        return self.list(request)


class ConstructorCreateApi(generics.CreateAPIView):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer


class ConstructorViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         GenericViewSet):
    queryset = Constructor.objects.all()
    serializer_class = ConstructorSerializer
