from django.db import models


class Call(models.Model):
    id_call = models.CharField(max_length=255,blank=True)
    number = models.CharField(max_length=255)
    datetime = models.DateTimeField(blank=True)
    call_status = models.CharField(max_length=255,blank=True)
    call_type = models.CharField(max_length=255,blank=True)
    id_client = models.CharField(max_length=255,blank=True)
    name_client = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=255,blank=True)
    comment = models.CharField(max_length=255,blank=True)
    manager = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.number


