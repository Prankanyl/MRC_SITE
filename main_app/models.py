from django.db import models
# from PIL import Image


class Student(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Фамилия',
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name='Отчество',
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        verbose_name='Возраст',
    )
    course = models.IntegerField(
        verbose_name='Курс',
    )
    group = models.CharField(
        verbose_name='Группа',
        max_length=10,
    )
    specialty = models.CharField(
        verbose_name='Специальность',
        max_length=50,
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='main_app/image/students',
        default=None,
        blank=True,
        null=True,
    )
    code = models.IntegerField(
        verbose_name='Код учащегося',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Фамилия',
    )
    patronymic = models.CharField(
        max_length=20,
        verbose_name='Отчество',
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        null=True,
    )
    category = models.CharField(
        verbose_name='Категоря преподавателя',
        max_length=20
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='main_app/image/teachers',
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Specialty(models.Model):
    specialty_title = models.CharField(
        verbose_name='Название специальности',
        max_length=50,
    )
    specialty_descriptions = models.TextField(
        verbose_name='Описание специальности'
    )
    specialty_logo = models.ImageField(
        verbose_name='Логотип специальности',
        upload_to='main_app/image/logo',
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.specialty_title}'

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
