from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mynewapp import *
from mynewapp import *


# Create your views here.



def set_user_session(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')


        request.session['name'] = name
        request.session['email'] = email
        
       
        return render(request,'logout.html',{'name':name})
    return render(request, 'login.html')

def del_session(request):
    if request.method=='POST':
        del request.session['name']
        # return HttpResponse('deleted')
        return render(request,'login.html')
    
def get_s(request):
    x=request.session['name']
    return HttpResponse(x)




