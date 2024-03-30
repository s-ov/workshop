# Generated by Django 4.2.11 on 2024-03-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_works_repair_type_alter_repair_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Created'), ('CONFIRMED', 'Confirmed'), ('READY_TO_REPAIR', 'Ready to repair'), ('PROGRESS', 'In progress'), ('VERIFICATION', 'Verification'), ('TEST', 'Test'), ('RE_REPAIR', 'Re-repair')], default='CREATED', max_length=20, verbose_name='Статус'),
        ),
    ]