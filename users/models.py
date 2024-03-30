from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    CUSTOMER = 'CUSTOMER', 'Customer'
    TECHNICIAN = 'TECHNICIAN', 'Technician'
    MASTER = 'MASTER', 'Master'
    WORKER = 'WORKER', 'Worker'


class User(AbstractUser):
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.CUSTOMER)
    email = models.EmailField(_('email address'), max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
