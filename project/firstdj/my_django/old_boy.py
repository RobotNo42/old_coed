from django.shortcuts import HttpResponse, render, redirect
from utils import sqlheper
import json


def all_class(request):
    class_list = sqlheper.get_list("select id,classname from class", [])
    return render(request, 'class.html', {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        new_class = request.POST.get('new_class')
        sqlheper.modify("insert into class(classname) value (%s)", [new_class, ])
        return redirect('/class/')


def del_class(request):
    nid = request.GET.get('nid')
    sqlheper.modify("delete from class where id = %s", [nid, ])
    return redirect('/class/')


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlheper.get_one("select id ,classname from class where id = %s", [nid, ])
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        new_class_name = request.POST.get('new_class_name')
        sqlheper.modify("update class set classname = %s where id = %s", [new_class_name, nid, ])
        return redirect('/class/')


def student(request):
    cookies = request.COOKIES.get('ticket')
    if not cookies:
        return redirect('/loginhou/')
    student_list = sqlheper.get_list("select student.id , student.name, student.classname as class_name,class.classname from student left join class on student.classname=class.id order by student.id asc ", [])
    class_list = sqlheper.get_list("select id, classname from class", [])
    return render(request, 'student.html', {'student_list': student_list, 'class_list': class_list})


def add_student(request):
    if request.method == "GET":
        class_list = sqlheper.get_list("select id,classname from class", [])
        return render(request, 'add_student.html', {'class_list': class_list})
    else:
        new_name = request.POST.get('new_student')
        new_class = request.POST.get('select_class')
        sqlheper.modify("insert into student(name,classname) values(%s, %s)", [new_name, new_class, ])
        return redirect('/student/')


def del_student(request):
    nid = request.GET.get('nid')
    sqlheper.modify("delete from student where id = %s", [nid, ])
    return redirect('/student/')


def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlheper.get_one("select id ,name, classname from student where id = %s", [nid, ])
        class_list = sqlheper.get_list("select id,classname from class", [])
        return render(request, 'edit_student.html', {'result': result, 'class_list': class_list})
    else:
        nid = request.GET.get('nid')
        new_student_name = request.POST.get('new_student_name')
        new_class_name = request.POST.get('new_select')
        sqlheper.modify("update student set name=%s,classname = %s where id = %s", [new_student_name, new_class_name, nid, ])
        return redirect('/student/')


def model_add_class(request):
        new_class = request.POST.get('new_class')
        if len(new_class) > 0:
            sqlheper.modify("insert into class(classname) value (%s)", [new_class, ])
            return HttpResponse('OK')
        else:
            return HttpResponse('班级名称不能为空')


def model_edit_class(request):
    nid = request.POST.get('nid')
    new_class_name = request.POST.get('new_class_name')
    if len(new_class_name) > 0:
        sqlheper.modify("update class set classname = %s where id = %s", [new_class_name, nid, ])
        return HttpResponse('OK')
    else:
        return HttpResponse('班级名称不能为空')


def model_del_class(request):
    nid = request.POST.get('nid')
    try:
        sqlheper.modify("delete from class where id = %s", [nid, ])
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)


def mode_add_student(request):
    ret = {'status': True, 'message': None}
    try:
        new_name = request.POST.get('new_student')
        new_class = request.POST.get('select_class')
        sqlheper.modify("insert into student(name,classname) values(%s, %s)", [new_name, new_class, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def mode_edit_student(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        new_student_name = request.POST.get('new_student_name')
        new_class_name = request.POST.get('new_select')
        sqlheper.modify("update student set name=%s,classname = %s where id = %s", [new_student_name, new_class_name, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def mode_del_student(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        sqlheper.modify("delete from student where id = %s", [nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def teacher(request):
    class_list = sqlheper.get_list("""
    SELECT teacher.id as nid, teacher.name as teacher_name, class.classname as class_name from teacherclass
    LEFT JOIN teacher on teacherclass.teacher = teacher.id
    LEFT JOIN class on teacherclass.class = class.id order by teacher.id
    """, [])
    class_all = sqlheper.get_list('select id,classname from class', [])
    request_list = {}
    for re in class_list:
        nid = re['nid']
        if nid in request_list:
            request_list[nid]['class_name'].append(re['class_name'])
        else:
            request_list[nid] = {'nid': re['nid'],'teacher_name': re['teacher_name'], 'class_name': [re['class_name'], ]}
    return render(request, 'teacher.html', {'class_list': request_list.values(), 'class_all': class_all})


def mode_add_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('teacher_name')
        class_names = request.POST.getlist('class_name')
        print(name, class_names)
        teacher_id = sqlheper.creat_modify('insert into teacher(name) values(%s)', [name, ])
        data_list = []
        for re in class_names:
            temp = (teacher_id, re)
            data_list.append(temp)
        obj = sqlheper.SqlHelper()
        obj.multiple_modify('insert into teacherclass(teacher, class) values (%s,%s)', data_list)
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def mode_edit_teacher(request):
    pass


def mode_del_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        sqlheper.modify('delete from teacher where id = %s', [nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def inb(request):
    return render(request, 'in.html')


def test(request):
    return render(request, 'test.html')


def loginhou(request):
    if request.method == 'GET':
        return render(request, 'loginhou.html')
    else:
        user = request.POST.get('username')
        password = request.POST.get('passwd')
        if user == 'chengge1124' and password == '946971':
            obj = redirect('/student/')
            obj.set_cookie('ticket', 'fucku',max_age=10)
            return obj
        else:
            return render(request,'loginhou.html')