from django.db import models


class Locomotive(models.Model):
    name = models.CharField(max_length=55, verbose_name='Назва локомотиву')

    class Meta:
        verbose_name = 'Локомотив'
        verbose_name_plural = 'Локомотиви'

    def __str__(self):
        return self.name
