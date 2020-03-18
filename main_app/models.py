from django.db import models
from abc import ABC, abstractmethod


class Man(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя человека',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Фамилия человека',
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name='Отчество человека',
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=30,
        blank=True,
        null=True,
    )


class Student(Man):
    age = models.IntegerField(
        verbose_name='Возраст студента',
    )
    course = models.IntegerField(
        verbose_name='Курс студента',
    )
    group = models.CharField(
        verbose_name='Группа студента',
        max_length=10,
    )
    pass


class Teacher(Man):
    category = models.CharField(
        verbose_name='Категоря преподавателя',
        max_length=20
    )
    pass


class Specialty(models.Model):
    pass
