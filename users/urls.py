from django.urls import path

from users.views import HomeView, PaymentPendingView, OnBoardingView, authentication_redirect

app_name = 'users'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('onboarding/', OnBoardingView.as_view(), name="onboarding"),
    path('onboarding/payment-pending', PaymentPendingView.as_view(), name='payment_pending'),
    path('authentication/redirect', authentication_redirect, name='payment_pending'),

]
