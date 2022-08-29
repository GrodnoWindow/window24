from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from rest_framework import exceptions, viewsets, status, generics, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from core.pagination import CustomPagination
from .authentication import generate_access_token, JWTAuthentication
from .models import Permission, Role
from .serializers import UserSerializer, PermissionSerializer, RoleSerializer, UserRegistrationSerializer, \
    UserLoginSerializer

User = get_user_model()


class UserRegister(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    queryset = User.objects.all()


class UserLogin(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data=request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            # user_obj = authenticate(request, username=data['username'], password=data['password'])
            # login(request, user_obj)
            response = Response()
            token = serializer.data['token'],
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token,
            }
            response.status_code = status.HTTP_200_OK
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserLogout(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self):
#         # user = request.user
#         # if user.is_authenticated:
#         #     logout(request)
#         response = Response()
#         response.delete_cookie(key='jwt')
#         response.data = {
#             'message': 'Success'
#         }
#         return response

@api_view(['POST'])
def logout(_):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data= {
        'message': 'Success'
    }
    return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = UserSerializer(request.user).data
        # data['permissions'] = [p['name'] for p in data['role']['permissions']]
        return Response({
            'data': data
        })


class PermissionAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [JWTAuthentication]
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
            'role': request.data['role_id']
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

