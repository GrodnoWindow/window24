from django.db import models

# Create your models here.


class Client(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

