from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from school_m.models import *


# Create your views here.
def admin(request):
    return render(request,'admin.html')

def home(request):
    return render (request,'home.html')

def add_dept(request):
    if request.method == 'GET':
        return render(request,'add_department.html')
    else:
        dep = request.POST['dept']

        data = Department.objects.create(department_name=dep)
        data.save()
        return render(request,'admin.html')
    

def view_dep(request):
    data =Department.objects.all()
    return render(request,'depart.html',{'data':data})


def studentReg(request):
    if request.method == 'GET':
        dep = Department.objects.all()
        return render(request,'studentreg.html',{'dep':dep})
    else:
        f = request.POST['fname']
        l = request.POST['lname']
        a = request.POST['age']
        e = request.POST['email']
        ph = request.POST['phone']
        u = request.POST['uname']
        p = request.POST['pswd']
        d = request.POST['depart']
        user_data =User.objects.create(first_name = f,
                                       last_name = l,
                                       email = e,
                                       user_type='STUDENT',
                                       username = u,
                                       password = p,
                                       is_active = False)
        user_data.save()
        stud_data = Student1.objects.create(age = a,
                                            phone = ph,
                                            department_id_id = d,
                                            stud_id_id = user_data.id)
        stud_data.save()
        return render(request,'home.html')
    
def student_view(request):
    data= Student1.objects.all()
    return render(request,'studentview.html',{'data':data})   