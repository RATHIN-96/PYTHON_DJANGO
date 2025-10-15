from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Newapp.forms import *

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

    