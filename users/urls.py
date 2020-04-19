from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from users.views import HomeView

app_name = 'users'
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]