from datetime import date

from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import *
from .filters import *


#  Create your views here.

class EmployeeListingPage(ListView):
    template_name = "emp_list.html"
    model = Employee
    context_object_name = "employees"
    paginate_by = 4

    # def get_context_data(self, *, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     employees = Employee.objects.f()


class EmployeeDetailPage(DetailView):
    template_name = "emp_detail.html"
    model = Employee
    context_object_name = "employee"


class EmployeeCreatePage(CreateView):
    template_name = "create_emp.html"
    form_class = EmployeeCreationForm
    success_url = "/employees/"


class EmployeeUpdatePage(UpdateView):
    model = Employee
    template_name = "update_emp.html"
    form_class = EmployeeCreationForm
    success_url = "/employees/"
    #
    # def get_queryset(self):
    #     context = super().get_context_data(**kwargs)
    #     if request.method =="POST":
    #


def delete_employee(request, pk):
    emp_del = Employee.objects.get(pk=pk)
    emp_del.delete()
    return redirect("/employees/")


def test(request):
    filtered_persons = PersonFilter(
        request.GET,
        queryset=Employee.objects.all()
    )
    context = {
        'filtered_persons': filtered_persons
    }
    return render(request, "test.html", context=context)


class Dasboardview(TemplateView):
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

# class TestTemplate(TemplateView):
#     template_name = "testing.html"
#
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         rest= Employee.objects.all()
#         context['test']= Employee.objects.all()
#         context['count']= rest.count()
# context['today'] = date.today()
#         return context
