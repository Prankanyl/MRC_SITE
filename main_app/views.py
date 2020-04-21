from django.shortcuts import render
from .models import (
    Student,
    Teacher,
    Specialty,
    Practice,
    Timetable
)
from news_app.models import Article


def base_page(request):
    specialty = Specialty.objects.all()
    articles = Article.objects.order_by('-date_release')[:3]
    return render(request, 'main_app/base.html', context={'articles': articles, 'specialty': specialty})


def timetable_page(request):
    timetable_groups = Timetable.objects.order_by('-course')
    course_groups = list()
    for item in timetable_groups:
        if item.course not in course_groups:
            course_groups.append(item.course)
    # course_groups = sorted(course_groups, reverse=True)
    course_groups.sort(reverse=True)
    return render(request, 'main_app/timetable.html', context={'timetable_groups': timetable_groups, 'course_groups': course_groups})


def history_page(request):
    return render(request, 'main_app/history_mrc.html', context={})


def specialty_page(request, specialty_id):
    specialty_item = Specialty.objects.get(id=specialty_id)
    specialty_list = specialty_item.specialty_descriptions.split('\n')
    return render(request, 'main_app/specialty.html', context={'specialty_item': specialty_item, 'specialty_list': specialty_list})


def specialty_information_page(request):
    specialty = Specialty.objects.all()
    arr_specialty_list = list()
    for item in specialty:
        tmp = item.specialty_descriptions.split('\n')
        arr_specialty_list.append(tmp)
    return render(request, 'main_app/specialty_information.html', context={'specialty': specialty, 'arr_specialty_list': arr_specialty_list})


def contacts_page(request):
    return render(request, 'main_app/contacts.html', context={})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'main_app/list_students.html', context={'students': students})


def structure_mrc(request):
    return render(request, 'main_app/structure_mrc.html', context={})


def practice(request):
    all_practice = Practice.objects.all()
    specialty_practice = list()
    for item in all_practice:
        if item.specialty not in specialty_practice:
            specialty_practice.append(item.specialty)
    return render(request, 'main_app/practice.html', context={'all_practice': all_practice, 'specialty_practice': specialty_practice})


def question(request):
    return render(request, 'main_app/question.html', context={})


def documents(request):
    return render(request, 'main_app/documents.html', context={})


def courses(request):
    return render(request, 'main_app/courses.html', context={})
