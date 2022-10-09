from django.db import models

# Create your models here.
class Department(models.Model):
    DepId = models.IntegerField('Department ID')
    DepName = models.CharField('Department Name', max_length=120) 

    def __str__(self):
        return self.DepName

class Employee(models.Model):
    EmpID = models.IntegerField('Employee ID',max_length=10)
    EmpName = models.CharField('Employee Name', max_length=120)
    Salary = models.IntegerField('Salary',max_length=4) 
    Manager = models.CharField('Manager',max_length=300)
    Location = models.CharField('Location',max_length=15)
    DepartmentID = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.EmpName