from django.db import models


class Call(models.Model):
    id_call = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255,blank=True)
    id_client = models.CharField(max_length=255,blank=True)
    name_client = models.CharField(max_length=255,blank=True)
    # client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=255,blank=True)
    manager = models.CharField(max_length=255,blank=True)


    def __str__(self):
        return self.number


