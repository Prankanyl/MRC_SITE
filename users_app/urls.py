from django.urls import path, reverse_lazy, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    sing_in_or_up_page,
    personal_area,
)


app_name = 'users_app'

urlpatterns = [
    path('login/personal_area', personal_area, name='personal_area'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='users_app/sing_in_or_up.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users_app:login')), name='logout'),
]
