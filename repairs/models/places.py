from django.db import models


class PlacesToWork(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва місця')

    class Meta:
        verbose_name = 'Місце роботи'
        verbose_name_plural = 'Місця роботи'

    def __str__(self):
        return self.name
