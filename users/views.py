from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


from core.pagination import CustomPagination
from utils.authentication import JWTAuthenticationApp
from django.contrib.auth.models import Permission, Group
from .models import User
from .serializers import UserSerializer, PermissionSerializer, GroupSerializer, \
    UserRegistrationSerializer


@api_view(['POST'])
def register(request):
    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match!')

    serializer = UserRegistrationSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        data = UserSerializer(request.user).data
        # data['permissions'] = [p['name'] for p in data['groups']['user_permissions']]
        return Response({
            'data': data
        })


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]
    serializer_class = PermissionSerializer

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })


class GroupViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]
    serializer = GroupSerializer

    def list(self, request):
        serializer = GroupSerializer(Group.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = GroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        group = Group.objects.get(id=pk)
        serializer = GroupSerializer(group)

        return Response({
            'data': serializer.data
        })

    def update(self, request, pk=None):
        role = Group.objects.get(id=pk)
        serializer = GroupSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        role = Group.objects.get(id=pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })

        return self.list(request)

    def post(self, request):
        request.data.update({
            'password': 1234,
            # 'role': request.data['role_id']
        })
        return Response({
            'data': self.create(request).data
        })

    def put(self, request, pk=None):

        # if request.data['role_id']:
        #     request.data.update({
        #         'role': request.data['role_id']
        #     })

        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ProfileUserInfoAPIView(APIView):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileChangePasswordAPIView(APIView):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def put(self, request, pk=None):
        user = request.user

        if request.data['password'] != request.data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        user.set_password(request.data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
