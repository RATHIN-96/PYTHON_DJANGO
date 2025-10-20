from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from myapp.forms import StudForm,EmpForm
from myapp.models import *
# Create your views here.
def first(request):
    return HttpResponse('Welcome To Django ...')

def load_index1(request):
    temp=loader.get_template('index1.html')
    stud={'name':'ammu'}

    

    return HttpResponse(temp.render( stud )) 

def loading(request):
    n=input('enter your name: ')
    val={'na':n}
    pyt={'co':'Python'}
    context = {**val, **pyt}
    return render(request,'index1.html',context)

    
def  index2 (request):
    return render(request,'index2.html')

def stud_reg(request):
    stud=StudForm
    return render(request,'stud.html',{'stud':stud})


# def  emp_reg (request):
#      emp=empform()
#      return render (request,'four.html',{'emp':emp})


def emp_reg(request):
    if request.method == "GET":

        emp=EmpForm()
        return render (request,'emp.html',{'emp':emp})
    else:
        data =EmpForm (request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Data Saved !')
        else:
            return HttpResponse('Failed')

def file_up(request):
    if request.method == 'GET':
        return render(request,'file.html')
    else:
        n = request.POST['name']
        f = request.FILES['file']
        data = File_Upload.objects.create(name=n,photo=f)
        data.save()
        return HttpResponse('data uploaded')
    
def create_s(request):
    request.session['name']='Ammu'
    request.session['email']='ammu@gmail.com'
    return HttpResponse('session Created')

def get_s(request):
    x = request.session['name']
    y = request.session['email']
    return HttpResponse(x+''+y)

def del_s(request):
    del request.session['name']
    return HttpResponse('Deleted')

def set_cookie(request):
    res = HttpResponse('cookies created')
    res.set_cookie('name','Rohan')
    return res

def get_cookie(request):
    x = request.COOKIES['name']
    return HttpResponse(x)

def teach_reg(request):
    if request.method == 'GET':
        return render(request,'teachr_reg.html')
    else:
        fn = request.POST['fname']
        ln = request.POST['lname']
        a = request.POST['age']
        e = request.POST['email']
        data = Teacher.objects.create(first_name =fn , last_name =ln , age =a , email =e)
        data.save()
        return HttpResponse ("<script>alert('Successfully Registered');window.location.href='/tview/';</script>"
)
    
def teach_view(request):
    data = Teacher.objects.all()
    return render(request,'teachr_view.html',{'data':data})


def del_teacher(request,i):
    data=Teacher.objects.get(id=i)
    data.delete()
    return HttpResponse ("<script>alert('Successfully Deleted !');window.location.href='/tview/';</script>")

def up_teach(request,i):
    if request.method == 'GET':
        data=Teacher.objects.get(id=i)
        return render (request,'teacherpro.html',{'data':data})
    else:
        teacher=get_object_or_404(Teacher,id=i)
        teacher.first_name = request.POST['fname']
        teacher.last_name = request.POST['lname']
        teacher.age = request.POST['age']
        teacher.email = request.POST['email']
        teacher.save()
        return redirect(teach_view)
