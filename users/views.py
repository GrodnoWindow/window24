from django.conf import settings

from django.middleware import csrf
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.pagination import CustomPagination
from .authentication import JWTAuthenticationApp
# from django.contrib.auth.models import Permission, ContentType
from .models import Role, User, Permission
from .serializers import UserSerializer, PermissionSerializer, RoleSerializer, LoginSerializer, LogoutSerializer, \
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


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        response = Response()
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            tokens = serializer.data["tokens"]
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=tokens["access"],
                # expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = serializer.data
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = Response()
        response.delete_cookie(key='access_token')
        response.delete_cookie(key='csrftoken')

        serializer.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        data = UserSerializer(request.user).data
        data['permissions'] = [p['name'] for p in data['role']['permissions']]
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


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthenticationApp]
    permission_classes = [IsAuthenticated]
    serializer = RoleSerializer

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)

        return Response({
            'data': serializer.data
        })

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        role = Role.objects.get(id=pk)
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

        if request.data['role_id']:
            request.data.update({
                'role': request.data['role_id']
            })

        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ProfileUserInfoAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileChangePasswordAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user

        if request.data['password'] != request.data['password_confirm']:
            raise exceptions.ValidationError('Passwords do not match')

        user.set_password(request.data['password'])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
