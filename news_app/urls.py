from django.urls import path
from .views import (
    news_page,
    news,
    leave_comment,
)


app_name = 'news_app'

urlpatterns = [
    path('all_news/', news_page, name='news_page'),
    path('all_news/<int:article_id>/', news, name='news'),
    path('all_news/<int:article_id>/leave_comment', leave_comment, name='leave_comment'),
]
