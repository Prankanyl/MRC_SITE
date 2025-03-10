from django.urls import path
from .views import (
    base_page,
    timetable_page,
    history_page,
    specialty_page,
    specialty_information_page,
    list_students,
    structure_mrc,
    practice,
    question,
    documents,
    contacts_page,
    courses,
)


app_name = 'main_app'

urlpatterns = [
    path('', base_page, name='base_page'),
    path('timetable/', timetable_page, name='timetable_page'),
    path('history_mrc/', history_page, name='history_page'),
    path('specialty_information/<int:specialty_id>', specialty_page, name='specialty_page'),
    path('specialty_information/', specialty_information_page, name='specialty_information_page'),
    path('list_students/', list_students, name='list_students'),
    path('structure_mrc/', structure_mrc, name='structure_mrc'),
    path('practice/', practice, name='practice'),
    path('question/', question, name='question'),
    path('documents/', documents, name='documents'),
    path('contacts/', contacts_page, name='contacts_page'),
    path('courses/', courses, name='courses'),
]
