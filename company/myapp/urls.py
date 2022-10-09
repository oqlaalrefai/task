from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('employee',views.all_employees, name='list-employees'),
    path('department', views.all_departments, name='list-departments'),
    # url(r'^dep/(?P<dep_id>[0-9]+)',views.all_departments, name='list-departments'),
    path('addemp', views.add_emp, name='add-emp'),
    path('adddep', views.add_dep, name='add-dep'),
    path('department/<depid>', views.show_dep, name='show-dep'),
]