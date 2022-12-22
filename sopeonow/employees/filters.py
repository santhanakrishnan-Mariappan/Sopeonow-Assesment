import django_filters

from .models import *



class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields =  [
            'Name',
            # 'post',
            # 'Department',
        ]