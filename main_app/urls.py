from django.urls import path
from .views import (
    base_page,
    timetable_page,
    history_page
)


app_name = 'main_app'

urlpatterns = [
    path('', base_page, name='base_page'),
    path('timetable/', timetable_page, name='timetable_page'),
    path('history_mrc/', history_page, name='history_page')
]
