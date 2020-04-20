from django.shortcuts import render
from .models import Article, Comment


def news_page(request):
    articles = Article.objects.order_by('-date_release')
    return render(request, 'news_app/news_page.html', context={'articles': articles})


def news(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'news_app/news.html', context={'article': article})
