from django.test import TestCase
from .models import Student, Teacher

# Create your tests here.


class MyTestClass(TestCase):
    # def setUp(self):
    #     self.Student = Student.objects.create(first_name='', )
    def test_1(self):
        self.Student = Student.objects.create(first_name='', last_name='')

    def test_2(self):
        self.Student = Student.objects.create(
            first_name='first_name',
            last_name='last_name',
            patronymic='patronymic',
            age=18,
            course=3,
            specialty='POIT',
            code=1,
        )

    def test_3(self):
        self.Student = Student.objects.create(
            first_name='first_name1111111111111111111111111111111',
            last_name='last_name',
            patronymic='patronymic',
            age=18,
            course=3,
            specialty='POIT',
            code=1,
        )

    def test_4(self):
        self.Student = Teacher.objects.create(
            first_name='first_name',
            last_name='last_name',
            patronymic='patronymic',
            category='12'
        )
