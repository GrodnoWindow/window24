from django.contrib.auth.models import Group
from auth_groups.serializers import GroupSerializer
from utils import crud


class GroupDetail(crud.RetrieveMixin,
                  crud.UpdateMixin,
                  crud.DeleteMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupList(crud.RetrieveListMixin,
                crud.CreateMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
