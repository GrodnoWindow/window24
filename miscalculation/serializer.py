from rest_framework import serializers, status

from .models import *


class MiscalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miscalculation
        fields = ['id', 'author', 'constructors', 'sum', 'status',
                  'created_time', 'last_update_time']