# Create your views here.
from django.shortcuts import redirect
from django.views.generic import TemplateView

from users.models import User


class HomeView(TemplateView):
    template_name = 'account/home.html'


class OnBoardingView(TemplateView):
    template_name = 'program/onboarding_form.html'

    def get_context_data(self, **kwargs):
        context = super(OnBoardingView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PaymentPendingView(TemplateView):
    template_name = 'account/payment_pending.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentPendingView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


def authentication_redirect(request):
    user = User.objects.get(id=request.user.id)
    if user.on_boarding_complete:
        return redirect('program:dashboard')

    if user.personal_info_complete and user.family_medical_history_complete and user.person_medical_history_complete and user.associated_health_problems_complete and user.daily_routine_complete:
        if user.payment_complete:
            user.on_boarding_complete = True
            user.save()
            return redirect('program:dashboard')

        else:
            return redirect('users:payment_pending')

    else:
        return redirect('users:onboarding')
