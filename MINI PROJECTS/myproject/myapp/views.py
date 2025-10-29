from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from myapp.models  import *

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        n = request.POST['name']
        e = request.POST['email']
        p = request.POST['place']
        a = request.POST['age']
        nu = request.POST['number']
        data= Leader.objects.create(name=n,email=e,place=p,age=a,number=nu)
        data.save()
        return HttpResponse("<script>window.location.href='/vie/'</script>")
    
    
def view(request):
    data=Leader.objects.all()
    print(data)
    return render(request,'table.html',{'data':data})

def del_teacher(request , i):
    data = Leader.objects.get(id =i)
    data.delete()
    return HttpResponse("<script>window.alert (Sucessfully Deleted); window.location.href='/vie/';</script>")


