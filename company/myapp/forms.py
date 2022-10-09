from tkinter import Widget
from unicodedata import name
from django import forms
from django.forms import ModelForm, TextInput
from .models import Employee,Department

class EmployeeForm(ModelForm) :
    class Meta:
        model = Employee
        fields = ('EmpID','EmpName', 'Salary', 'Manager', 'Location','DepartmentID')
        widgets = {
            'EmpID':forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}),
            'EmpName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'Salary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Salary'}),
            'Manager':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager'}),
            'Location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
            'DepartmentID':forms.Select(attrs={'class':'form-control', 'placeholder':'Department'}),
        }


class DepartemntForm(ModelForm):
    class Meta:
        model = Department
        fields = ('DepId','DepName')
        widgets = {
            'DepId':forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}),
            'DepName': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}),
        }
        