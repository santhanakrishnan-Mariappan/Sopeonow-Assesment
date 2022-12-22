from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeListingPage.as_view(), name="emp-list"),
    # path('dashboard/', Dasboardview.as_view(), name="dashboard"),
    path('<int:pk>/', EmployeeDetailPage.as_view(), name="emp-detail"),
    path('create/', EmployeeCreatePage.as_view(), name="emp-create"),
    path('edit/<int:pk>', EmployeeUpdatePage.as_view(), name="emp-edit"),
    path('delete/<int:pk>', delete_employee, name="emp-delete"),
    path('test', test, name="test"),

]
