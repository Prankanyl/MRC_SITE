from django.urls import path
from .views import (
    news_page,
)


app_name = 'news_app'

urlpatterns = [
    path('news/', news_page, name='news_page'),
]
