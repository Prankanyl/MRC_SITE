from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    login = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Профиль пользователя'
    )
    password = models.CharField(
        max_length=20,
        verbose_name='Пароль'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = (
            'login',
        )
