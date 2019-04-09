"""firstdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path, re_path
from my_django import old_boy, lb, test


urlpatterns = [
    path('test/', old_boy.test),
    path('lb/', lb.lb),
    path('login/', lb.login),
    path('class/', old_boy.all_class),
    path('add_class/', old_boy.add_class),
    path('del_class/', old_boy.del_class ),
    path('edit_class/', old_boy.edit_class),
    path('student/', old_boy.student),
    path('add_student/', old_boy.add_student),
    path('del_student/', old_boy.del_student),
    path('edit_student/', old_boy.edit_student),
    path('model_add_class/', old_boy.model_add_class),
    path('model_edit_class/', old_boy.model_edit_class),
    path('model_del_class/', old_boy.model_del_class),
    path('model_add_student/', old_boy.mode_add_student),
    path('model_edit_student/', old_boy.mode_edit_student),
    path('model_del_student/', old_boy.mode_del_student),
    path('teacher/', old_boy.teacher),
    path('model_add_teacher/', old_boy.mode_add_teacher),
    path('model_edit_teacher/', old_boy.mode_edit_teacher),
    path('model_del_teacher/', old_boy.mode_del_teacher),
    path('in/', old_boy.inb),
    re_path(r'work(\w+)/', test.work),
    path('loginhou/', old_boy.loginhou)
]
