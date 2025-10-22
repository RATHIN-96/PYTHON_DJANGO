from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from school_m.models import *


# Create your views here.
def admin(request):
    return render(request,'admin.html')

def add_dept(request):
    if request.method == 'GET':
        return render(request,'add_department.html')
    else:
        dep = request.POST['dept']

        data = Department.objects.create(department_name=dep)
        data.save()
        return HttpResponse('success')
    