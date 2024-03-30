from django.db import models


class Works(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва роботи')
    repair_type = models.ForeignKey('repairs.RepairType', on_delete=models.CASCADE, related_name='works', 
                                    null=True, blank=True)

    class Meta:
        verbose_name = 'Робота'
        verbose_name_plural = 'Роботи'

    def __str__(self):
        return self.name
