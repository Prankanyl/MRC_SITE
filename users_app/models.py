from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    login = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Профиль пользователя'
    )

    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True,
    )

    address = models.CharField(
        verbose_name='Адресс',
        max_length=256,
        blank=True,
        null=True,
    )

    password = models.CharField(
        max_length=20,
        verbose_name='Пароль',
        blank=True,
        null=True,
    )
    position = models.CharField(
        max_length=256,
        verbose_name='Должность',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = (
            'login',
        )
