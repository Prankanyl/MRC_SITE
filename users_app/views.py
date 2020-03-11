from django.shortcuts import render


def sing_in_or_up_page(request):
    return render(request, 'users_app/sing_in_or_up.html', context={})
