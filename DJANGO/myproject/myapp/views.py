from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

    

