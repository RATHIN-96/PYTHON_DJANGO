"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first',views.first),

    path('index1/', views.load_index1),

    path('load2/',views.loading),

    path('js/',views.index2),

    path('stud/',views.stud_reg),
    
    path('emp/',views.emp_reg),

    path('file/',views.file_up),


    path('create_s/',views.create_s),

    path('get_s/',views.get_s),

    path('del/',views.del_s),

    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),

    path('treg/',views.teach_reg),
    path('tview/',views.teach_view),

    path('del/<int:i>',views.del_teacher),
    path('update/<int:i>',views.up_teach),


]
