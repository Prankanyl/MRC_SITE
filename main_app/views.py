from django.shortcuts import render


def base_page(request):
    return render(request, 'main_app/base.html', context={})


def timetable_page(request):
    return render(request, 'main_app/timetable.html', context={})


def history_page(request):
    return render(request, 'main_app/history_mrc.html', context={})


def specialty_page(request):
    return render(request, 'main_app/specialty.html', context={})


def specialty_information_page(request):
    return render(request, 'main_app/specialty_information.html', context={})


def contacts_page(request):
    return render(request, 'main_app/contacts.html', context={})

