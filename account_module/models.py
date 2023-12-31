from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='User Avatar', null=True ,blank=True)
    email_active_code = models.CharField(max_length=100 , verbose_name='Activator_Key')
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_full_name()