
from django.shortcuts import render
from .models import Department,Employee
from .forms import EmployeeForm,DepartemntForm
from django.http import HttpResponseRedirect

# Create your views here.
def all_employees(request):
    employee_list = Employee.objects.all()
    return render(request,'employeeList.html', {'employee_list':employee_list})

def all_departments(request):
    department_List = Department.objects.all()
    return render(request, 'Dep.html', {'department_List':department_List} )


def show_dep(request,depid):
    department_List = Department.objects.get(id=depid)
    department = Department.objects.get(id=depid)
    emp_dep = department.employee_set.all()
    empNames = emp_dep.values_list('EmpName')
    print(empNames, department_List)
    return render(request, 'showDep.html', {'department_List':department_List, 'empNames':empNames} )
    

def add_emp(request):
    submitted = False
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('addemp?submitted=True')
    else:
        form= EmployeeForm
        if 'submitted' in request.GET:
            submitted =True

    return render(request, 'AddEmp.html', {'form':form, 'submitted':submitted})

def add_dep(request):
    submitted = False
    if request.method == 'POST':
        form = DepartemntForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adddep?submitted=True')
    else:
        form= DepartemntForm
        if 'submitted' in request.GET:
            submitted =True

    return render(request, 'AddDep.html', {'form':form, 'submitted':submitted})