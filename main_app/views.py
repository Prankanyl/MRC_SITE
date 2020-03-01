from django.shortcuts import render


def base_page(request):
    return render(request, 'main_app/base.html', context={})

