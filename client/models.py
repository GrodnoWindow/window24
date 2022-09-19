from django.db import models
from call.models import Call

# Create your models here.


class Client(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    calls = models.ForeignKey(Call, on_delete=models.CASCADE, related_name='Calls',blank=True, null=True)

    def __str__(self):
        return self.name
