# Create your views here.
from django.views.generic import TemplateView


# Todo: Add permissions to endpoints
class DashboardView(TemplateView):
    template_name = 'program/dashboard.html'
