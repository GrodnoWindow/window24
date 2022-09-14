from django.db import models


class Call(models.Model):
    id_call = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    call_status = models.CharField(max_length=255,blank=True)
    call_type = models.CharField(max_length=255,blank=True)
    id_client = models.CharField(max_length=255,blank=True)
    name_client = models.CharField(max_length=255,blank=True)
    comment = models.CharField(max_length=255,blank=True)
    manager = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.number


