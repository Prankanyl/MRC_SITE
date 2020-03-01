from django.contrib import admin
from django.urls import path
from .views import (
    base_page,
)

urlpatterns = [
    path('', base_page, name='base_page'),
]
