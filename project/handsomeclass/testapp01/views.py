from django.shortcuts import render, HttpResponse, redirect
from testapp01 import models
from django.forms import Form
from django.forms import fields
from django.forms import widgets


class ClassForm(Form):
    title = fields.RegexField('^全栈\d+', error_messages={
        'invalid': '必须要以全栈+数字创建'
    })


class StudentForm(Form):
    name = fields.CharField(max_length=64, label='姓名')
    email = fields.EmailField(max_length=64, label='邮箱')
    age = fields.IntegerField(min_value=5, max_value=80, label='年龄')
    cls_id = fields.IntegerField(
        label='班级',
        widget=widgets.Select(choices=models.Class.objects.values_list('id', 'title'))
    )
    class_price = fields.IntegerField(label='价格')


def class_list(request):
    cls_list = models.Class.objects.all()
    return render(request, 'class.html', {'cls_list': cls_list, 'mes_in': '班级管理'})


def add_class(request):
    if request.method == "GET":
        obj = ClassForm()
        return render(request, 'add_class.html', {'obj': obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Class.objects.create(**obj.cleaned_data)
            return redirect('/class/')
        return render(request, 'add_class.html', {'obj': obj})


def edit_class(request, nid):
    if request.method == 'GET':
        row = models.Class.objects.filter(id=nid).first()
        obj = ClassForm(initial={'title': row.title})
        return render(request, 'edit_class.html', {'nid': nid, 'obj': obj})
    else:
        obj = ClassForm(request.POST)
        if obj.is_valid():
            models.Class.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/class/')
        return render(request, 'edit_class.html', {'obj': obj, 'nid': nid})


def del_class(request, nid):
    models.Class.objects.filter(id=nid).delete()
    return redirect('/class/')


def student(request):
    student_list = models.Student.objects.all()
    return render(request, 'student.html', {'student_list': student_list, 'mes_in': '学生管理'})


def add_student(request):
    if request.method == 'GET':
        obj = StudentForm()
        return render(request, 'add_student.html', {'obj': obj})


def teacher(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher_list': teacher_list, 'mes_in': '老师管理'})
