from datetime import datetime
from django import forms
from django.forms import ModelForm, widgets, ClearableFileInput
from django.core.exceptions import ValidationError

from .models import *
from django import forms


class FileInput(forms.FileInput):
    input_type = "file"

class DateInput(forms.DateInput):
    input_type = "date"


class EmployeeCreationForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('Name', 'post', 'DOB', 'DOJ', 'Department', 'Address', 'City', 'Country', 'ZipCode', 'dp', 'State',
                  'Leave_count', 'on_leave')

        def clean(self, *args, **kwargs):
            super(EmployeeCreationForm, self).clean(*args, **kwargs)
            today = datetime.datetime.today()
            Name = self.cleaned_data.get('Name', None)
            DOB = self.cleaned_data.get('DOB')

            if Name is not None and not Name.isalpha():
                raise forms.ValidationError('error')

            if DOB < today:
                raise ValidationError('Start time must be later than now.')

            return self.cleaned_data

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'fc form-control form-control-sm '}),
            'post': forms.TextInput(attrs={'class': 'form-control form-control-sm fc'}),
            'DOB': DateInput(attrs={'class': 'form-control form-control-sm', 'min' : 'date.today()'}),
            'DOJ': DateInput(attrs={'class': 'form-control form-control-sm', 'min' : 'date.today()'}),
            'Department': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'Address': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'City': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'Country': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'ZipCode': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            # 'dp': forms.FileInput(),
            'dp': forms.widgets.FileInput(),
            'State': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'Leave_count': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'on_leave': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        #


