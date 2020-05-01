# Create your views here.
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'program/dashboard.html'


class OnBoardingView(TemplateView):
    template_name = 'program/onboarding_form.html'

    def get_context_data(self, **kwargs):
        context = super(OnBoardingView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
