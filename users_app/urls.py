from django.urls import path
from .views import (
    sing_in_or_up_page,
)


app_name = 'users_app'

urlpatterns = [
    path('singinorup/', sing_in_or_up_page, name='sing_in_or_up_page'),
]
