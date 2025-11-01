"""
URL configuration for school_management project.

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
from school_m import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addmin/', views.admin),
    path('add_dpt/', views.add_dept),
    path('view_dpt/', views.view_dep),
    path('dep_del/<int:id>/', views.department_reject),
    path('registration/', views.Registration),
    path('', views.home),
    path('hm', views.home),
    path('stud_approve/<int:id>/', views.stud_approve, name='stud_approve'),
    path('studentview/', views.student_view, name='studentview'),
    path('stud_del/<int:id>', views.student_reject),
    path('login/', views.loginData),
    path('logout/', views.lgout),
    path('studedit/', views.stud_edit),
    path('studupdate/<int:ids>', views.stud_update),
    path('teacherview/', views.teacher_view, ),








]





# path('stud_approve/<int:id>/', views.stud_approve, name='stud_approve'),
# path('studentview/', views.student_view, name='studentview'),