from django.contrib.auth.models import Permission
from .serializers import PermissionSerializer
from utils import crud


class PermissionDetail(crud.RetrieveMixin,
                       crud.UpdateMixin,
                       crud.DeleteMixin):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PermissionList(crud.RetrieveListMixin,
                     crud.CreateMixin):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
