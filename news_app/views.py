from django.shortcuts import render
from .models import Article, Comment


def news_page(request):
    articles = Article.objects.all()
    return render(request, 'news_app/news_page.html', context={articles : articles})
