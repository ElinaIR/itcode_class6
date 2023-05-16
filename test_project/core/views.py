from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def home(request):
    return HttpResponse(content='Home sweet home')


def emp_list(request):
    emps = Employee.objects.all()
    posts = Post.objects.all()
    return render(request, 'core/list.html', context={'title': 'Список сотрудников', 'emps': emps, 'posts': posts})


def emp(request):
    emp = Employee.objects.get(id=request.GET.get('id'))
    post = Post.objects.get(id=emp.post.id)
    return render(request, 'core/employee.html', context={'title': 'Сотрудник', 'emp': emp, 'post': post})
