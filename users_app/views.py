from django.shortcuts import render
from django.contrib.auth.models import User
from main_app.models import Student, Teacher


def sing_in_or_up_page(request):
    return render(request, 'users_app/sing_in_or_up.html', context={})


def personal_area(request):
    user_id = request.POST
    user = False
    man = False
    # if user_id:
    #     user = User.objects.get(id=user_id)
    #     man = Student.objects.get(login_id=user_id)
    return render(request, 'users_app/personal_area.html', context={'user': user, 'man': man, 'user_id': user_id})
