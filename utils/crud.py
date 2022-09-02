from __future__ import absolute_import, unicode_literals
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
# from .permissions import CustomObjectPermissions
from utils.authentication import JWTAuthenticationApp
# Create



class CreateMixin(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, CustomObjectPermissions)
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # Override single and batch add
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Read single item data
class RetrieveMixin(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, CustomObjectPermissions)
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Read all items data
class RetrieveListMixin(mixins.ListModelMixin,
                        generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, CustomObjectPermissions)
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Update
class UpdateMixin(mixins.UpdateModelMixin,
                  generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, CustomObjectPermissions)
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# Delete
class DeleteMixin(mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    # permission_classes = (IsAuthenticated, CustomObjectPermissions)
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data=[], status=status.HTTP_200_OK)
