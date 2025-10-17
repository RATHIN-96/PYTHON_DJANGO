from django.shortcuts import render
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
    