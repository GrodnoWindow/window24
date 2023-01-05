from django.db import models



class Call_Okna(models.Model):
    id_call = models.CharField(max_length=255, blank=True)


class Call(models.Model):
    id_call = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255)
    datetime = models.DateTimeField(blank=True)
    call_status = models.CharField(max_length=255, blank=True)
    call_type = models.CharField(max_length=255, blank=True)
    client_id = models.IntegerField(blank=True)
    comment = models.CharField(max_length=255, blank=True)
    manager = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.datetime} {self.number}'
