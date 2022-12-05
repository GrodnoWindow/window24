from django.db import models

from calculation.models import Constructor


class Miscalculation(models.Model):
    author = models.CharField(max_length=255, blank=True)
    constructors = models.ManyToManyField(Constructor, verbose_name="Просчеты конструкторов", blank=True)
    created_time = models.DateTimeField(blank=True)
    last_update_time = models.DateTimeField(blank=True)
    sum = models.FloatField(max_length=255, default=0.0)
    status = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'Просчет №{self.id} на сумму {self.sum}'

    class Meta:
        verbose_name = 'Просчет'
        verbose_name_plural = 'Просчеты'
