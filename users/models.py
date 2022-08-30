from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class Permission(models.Model):
    name = models.CharField(max_length=200)


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


class User(AbstractUser):
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # email = models.CharField(max_length=200, unique=True)
    # password = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name='users', null=True)
    # username = None

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []


    @property
    def tokens(self) -> dict[str, str]:
        """Allow us to get a user's token by calling `user.token`."""
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}