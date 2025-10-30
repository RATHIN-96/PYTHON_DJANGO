from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login as auth_login,logout
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
        user_data =User.objects.create_user(first_name = f,
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
    
# def student_view(request):
#     data= Student1.objects.all()
#     return render(request,'studentview.html',{'data':data})   

def student_view(request):
    data = Student1.objects.filter(stud_id__is_active=False)  
    return render(request, 'studentview.html', {'data': data})

def stud_approve(request, id):
    student =Student1.objects.get(id=id)
    user = student.stud_id
    user.is_active = True
    user.save()
    

    return redirect('studentview')

# def student_approve(request,id):
#     stud = Student1.objects.get(id=id)
#     stud.stud_id.is_active = True
#     stud.stud_id.save()
#     # return redirect(student_view)
#     return HttpResponse('success')



def department_reject(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect(view_dep)

def student_reject(request,id):
    stud = Student1.objects.filter(id=id)
    user = Student1.objects.get(id=id)
    data = user.stud_id
    stud.delete()
    data.delete()
    return redirect('/studentview/')

def loginData(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        # print(uname,pswd)
        user = authenticate(request,username=uname,password=pswd)
        if user is not None and user.user_type == 'STUDENT' and user.is_active==True:
            auth_login(request,user)
            request.session['studid'] = user.id
            return render(request,'studentprofile.html')
        elif user is not None and user.is_superuser ==True:
            auth_login(request,user)
            request.session['adminid'] = user.id
            return render(request,'admin.html')
        else:
            return render(request,'login.html')

def lgout(request):
    logout(request)
    return redirect(loginData)
        
def stud_edit(request):
    if request.method == 'GET':
        stud = request.session.get('studid')
        print('session id.......................................hello: ',stud)
        userdata=User.objects.get(id=stud)
        data=Student1.objects.get(stud_id=userdata.id)
        return render(request,'studentedit.html',{'stud':data,'user':userdata})

def stud_update(request,ids):
    stud =Student1.objects.get(id=ids)
    sid = stud.stud_id
    user=User.objects.get(id=sid.id)
    user.first_name=request.POST['fname']
    user.last_name=request.POST['lname']
    user.email=request.POST['email']
    stud.age=request.POST['age']
    stud.phone=request.POST['phone']
    user.save()
    stud.save()
    return redirect('/studedit/')
