from django.db import models


class Parts(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва деталі')

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Деталі'

    def __str__(self):
        return self.name
