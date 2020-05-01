from django.contrib import admin
from django.urls import path, include

from program.views import DashboardView, OnBoardingView

app_name = "program"

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('onboarding/', OnBoardingView.as_view(), name="onboarding")
]