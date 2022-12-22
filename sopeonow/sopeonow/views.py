from django.shortcuts import render
from datetime import date
# Create your views here.
from django.views.generic import *

from employees.models import Employee


class LandingPageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.all()
        employees_active = Employee.objects.filter(Active=True)
        employees_on_leave = Employee.objects.filter(on_leave=True)
        context['Total_count'] = employees.count()
        context['employees_active'] = employees_active.count()
        context['employees_on_leave_count'] = employees_on_leave.count()
        context['today'] = date.today()
        return context