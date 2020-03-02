from django.shortcuts import render


def news_page(request):
    return render(request, 'news_app/news_page.html', context={})
