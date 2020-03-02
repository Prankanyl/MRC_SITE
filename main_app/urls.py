from django.urls import path
from .views import (
    base_page,
)


app_name = 'main_app'

urlpatterns = [
    path('', base_page, name='base_page'),
]
