from requests import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .serializer import *
from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from .utils import *
from config.pagination import CustomPagination

from call.models import Call


class ClientAPIView(APIView):

    serializer_class = ClientSerializer

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        client = Client.objects.create(
            name=request.data['name'],
            author=user, # get current user
        )
        number = create_number_record(request.data['number'])
        print(number)
        for num in number:
            client.number.add(num['id'])

        # calls = add_calls_to_client(request.data['number'])
        # client.calls.add(1)

        return Response({'client': request.data,})


class ClientViewSet(mixins.CreateModelMixin, # POST REQUESTS
                   mixins.RetrieveModelMixin, # get all, get<id>,
                   mixins.UpdateModelMixin, # put<id>, patch<id>
                   GenericViewSet):

    queryset = Client.objects.all() # .values().order_by('-id')
    serializer_class = ClientSerializer




