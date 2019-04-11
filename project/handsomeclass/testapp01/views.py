from django.shortcuts import render, HttpResponse, redirect
from testapp01 import models
from django.forms import Form
from django.forms import fields
from django.forms import widgets


class ClassForm(Form):
    title = fields.CharField(widget=widgets.TextInput(attrs={'class': 'form-control'}))


class StudentForm(Form):
    name = fields.CharField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    email = fields.EmailField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    age = fields.IntegerField(min_value=5, max_value=80, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    cls_id = fields.IntegerField(
        widget=widgets.Select(choices=models.Class.objects.values_list('id', 'title'), attrs={'class': 'form-control'})
    )


class TeacherForm(Form):
    name = fields.CharField(min_length=2, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    email = fields.EmailField(max_length=64, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    cls_id = fields.MultipleChoiceField(choices=models.Class.objects.values_list('id', 'title'),
                                        widget=widgets.SelectMultiple(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cls_id'].widget.choices = models.Class.objects.values_list('id', 'title')


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
    else:
        obj = StudentForm(request.POST)
        if obj .is_valid():
            models.Student.objects.create(**obj.cleaned_data)
            return redirect('/student/')
        return render(request, 'add_student.html', {'obj': obj})


def edit_student(request, nid):
    if request.method == 'GET':
        row = models.Student.objects.filter(id=nid).values('name', 'email', 'age', 'cls_id').first()
        obj = StudentForm(initial=row)
        return render(request, 'edit_student.html', {'obj': obj, 'nid': nid})
    else:
        obj = StudentForm(request.POST)
        if obj.is_valid():
            models.Student.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/student/')
        return render(request, 'edit_student.html', {'obj': obj, 'nid': nid})


def del_student(request, nid):
    models.Student.objects.filter(id=nid).delete()
    return redirect('/student/')


def teacher(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher_list': teacher_list, 'mes_in': '老师管理'})


def add_teacher(request):
    if request.method == 'GET':
        obj = TeacherForm()
        return render(request, 'add_teacher.html', {'obj': obj})
    else:
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            cls_id = obj.cleaned_data.pop('cls_id')
            row = models.Teacher.objects.create(**obj.cleaned_data)
            row.TtoC.add(*cls_id)
            return redirect('/teacher/')
        return render(request, 'add_teacher.html', {'obj': obj})


def edit_teacher(request, nid):
    if request.method == 'GET':
        row = models.Teacher.objects.filter(id=nid).first()
        class_id = row.TtoC.values_list('id')
        id_list = list(zip(*class_id))[0] if list(zip(*class_id)) else []
        obj = TeacherForm(initial={'name': row.name, 'email': row.email, 'cls_id': id_list})
        return render(request, 'edit_teacher.html', {'obj': obj, 'nid': nid})
    else:
        obj = TeacherForm(request.POST)
        if obj.is_valid():
            cls_id = obj.cleaned_data.pop('cls_id')
            models.Teacher.objects.filter(id=nid).update(**obj.cleaned_data)
            models.Teacher.objects.filter(id=nid).first().TtoC.set(cls_id)
            return redirect('/teacher/')
        return render(request, 'edit_teacher.html', {'obj': obj, 'nid': nid})


def del_teacher(request, nid):
    row = models.Teacher.objects.filter(id=nid).first()
    row.TtoC.remove(nid)
    row.delete()
    return redirect('/teacher/')