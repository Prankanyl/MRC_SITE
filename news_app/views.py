from django.shortcuts import render
from .models import Article, Comment


def news_page(request):
    return render(request, 'news_app/news_page.html', context={})
