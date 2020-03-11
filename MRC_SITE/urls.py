from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'), name='main_app'),
    path('', include('users_app.urls'), name='users_app'),
    path('', include('news_app.urls'), name='news_app'),
]

