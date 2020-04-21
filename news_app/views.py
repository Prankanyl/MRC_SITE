from django.shortcuts import render
from .models import Article, Comment
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect


def news_page(request):
    articles = Article.objects.order_by('-date_release')
    return render(request, 'news_app/news_page.html', context={'articles': articles})


def news(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Страница не найдена')
    list_context = article.article_text.split('\n')
    list_comments = article.comment_set.order_by('-id')
    return render(request, 'news_app/news.html', context={'article': article, 'list_context': list_context, 'list_comments': list_comments})


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404('Страница не найдена')
    article.comment_set.create(author_name=request.POST['author'], comment_text=request.POST['context'])
    return HttpResponseRedirect(reverse('news_app:news', args=(article_id,)))
