from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Newapp.forms import *
from Newapp.models import *

# Create your views here.


def first (request):
     return HttpResponse('HAI IAM NEW HERE')

def second (request):
     return HttpResponse('Save Money')

def load_index(request):

     tem=loader.get_template('one.html')

     

     ins=int(input('Enter a Number'))

     v={'name':'Rathin'}

     return HttpResponse(tem.render(v))


def index(request):

     tem=loader.get_template('one.html')

     

     ins=int(input('Enter a Number : '))

     v={'age':ins}



     return HttpResponse(tem.render(v))


def why (request):

     x=input('Enter your name: ')

     val={'na':x}
     return render(request,'one.html',val)


def two(request):
     return render(request,'two.html')


def stud_reg (request):
     stud = Student()

     return render(request,'three.html',{'stud':stud})

def  emp_reg (request):
     emp=empform()
     return render (request,'four.html',{'emp':emp})

def emp_reg(request):
     if request.method == 'GET':
          emp= empform()

          return render(request,'four.html',{'emp':emp})
     else:
          data = empform(request.POST)
          if data.is_valid():
               data.save()
               return HttpResponse('data saved !')
          else:
               return HttpResponse('failed  !')

def upload (request):
     if request.method == 'GET':
          return render(request,'day-5.html')
     # else:
     #      n = request.POST.get('name')
     #      f = request.FILES['file']

     #      data =File_Upload.objects.create(name=n,image=f)
     #      data.save()
     #      return HttpResponse('File upload Success')
     else:
        n = request.POST['name']
        f = request.FILES['files']
        data = File_Upload.objects.create(name=n,photo=f)
        data.save()
        return HttpResponse('data uploaded')
    