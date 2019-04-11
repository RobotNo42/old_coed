"""handsomeclass URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from testapp01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', views.class_list),
    path('add_class/', views.add_class),
    re_path('edit_class/(\d+)/', views.edit_class),
    re_path('del_class/(\d+)/', views.del_class),
    path('student/', views.student),
    path('add_student/', views.add_student),
    re_path('edit_student/(\d+)', views.edit_student),
    re_path('del_student/(\d+)', views.del_student),
    path('teacher/', views.teacher),
    path('add_teacher/', views.add_teacher),
    re_path('edit_teacher/(\d+)', views.edit_teacher),
    re_path('del_teacher/(\d+)', views.del_teacher),

]
