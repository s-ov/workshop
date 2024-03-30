from django.db import models
from django.urls import reverse

class Status(models.TextChoices):
    """"Statuses for repairs"""
    CREATED = 'CREATED', 'Created'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    READY_TO_WORK = 'READY_TO_REPAIR', 'Ready to repair'
    PROGRESS = 'PROGRESS', 'In progress'
    VERIFICATION = 'VERIFICATION', 'Verification'
    TEST = 'TEST', 'Test'
    RE_REPAIR = 'RE_REPAIR', 'Re-repair'



class Repair(models.Model):
    users = models.ManyToManyField(to='users.User', related_name='repairs', verbose_name='Заявники')
    description = models.TextField(verbose_name='Опис поломки')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED, verbose_name='Статус')
    time_to_work = models.DateTimeField(verbose_name='Час початку ремонту', null=True, blank=True)

    places_to_work = models.ForeignKey('repairs.PlacesToWork', related_name='place_repairs', verbose_name='Місця роботи',
                                       null=True, blank=True, on_delete=models.PROTECT)
    locomotive = models.ForeignKey('repairs.Locomotive', related_name='locomotive_repairs', verbose_name='Локомотив',
                                  null=True, blank=True, on_delete=models.PROTECT)
    repair_type = models.ForeignKey('repairs.RepairType', related_name='type_repairs', verbose_name='Тип ремонту',
                                    null=True, blank=True, on_delete=models.PROTECT)
    works = models.ManyToManyField(to='repairs.Works', related_name='work_repairs', verbose_name='Роботи')
    parts = models.ManyToManyField(to='repairs.Parts', related_name='parts_repairs', verbose_name='Деталі')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Заявка: {self.id}'
    
    def get_absolute_url(self):
        return reverse("repairs:detail", kwargs={"repair_id": self.pk})
    
