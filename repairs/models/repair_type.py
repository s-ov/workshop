from django.db import models


class RepairType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва типу ремонту')
    hours = models.IntegerField(verbose_name='Кількість годин ремонту')

    class Meta:
        verbose_name = 'Тип ремонту'
        verbose_name_plural = 'Типи ремонту'

    def __str__(self):
        return self.name
