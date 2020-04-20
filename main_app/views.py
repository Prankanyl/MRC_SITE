from django.shortcuts import render
from .models import (
    Student,
    Teacher,
    Specialty
)


def base_page(request):
    return render(request, 'main_app/base.html', context={})


def timetable_page(request):
    return render(request, 'main_app/timetable.html', context={})


def history_page(request):
    return render(request, 'main_app/history_mrc.html', context={})


def specialty_page(request):
    return render(request, 'main_app/specialty.html', context={})


def specialty_information_page(request):
    specialty = Specialty.objects.all()
    return render(request, 'main_app/specialty_information.html', context={'specialty': specialty})


def contacts_page(request):
    return render(request, 'main_app/contacts.html', context={})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'main_app/list_students.html', context={'students': students})


def structure_mrc(request):
    return render(request, 'main_app/structure_mrc.html', context={})


def practice(request):
    return render(request, 'main_app/practice.html', context={})


def question(request):
    return render(request, 'main_app/question.html', context={})


def documents(request):
    return render(request, 'main_app/documents.html', context={})
