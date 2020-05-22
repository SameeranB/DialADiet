from django.urls import path

from users.views import HomeView, PaymentPendingView, OnBoardingView, authentication_redirect, \
    PersonalInformationFormView

app_name = 'users'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('onboarding/', OnBoardingView.as_view(), name="onboarding"),
    path('onboarding/payment-pending', PaymentPendingView.as_view(), name='payment_pending'),
    path('onboarding/personal-information', PersonalInformationFormView.as_view(), name='personal_information_form'),
    path('authentication/redirect', authentication_redirect, name='auth_redirect'),

]
