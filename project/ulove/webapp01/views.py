from django.shortcuts import render,HttpResponse,redirect
from webapp01 import models
from django.forms import Form
from django.forms import fields


class MyForm(Form):
    username = fields.CharField(required=True, error_messages={
        'required': '用户名不能为空'
    })
    password = fields.CharField(required=True, error_messages={
     'required': '密码不能为空'
    })


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        obj = MyForm(request.POST)
        if obj.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            sex = request.POST.get('sex')
            if sex == '男':
                obj = models.Man.objects.filter(username=username, password=password).first()
            else:
                obj = models.Woman.objects.filter(username=username, password=password).first()
            if not obj:
                return render(request, 'login.html', {'message': '用户名或密码错误'})
            else:
                request.session['username'] = obj.username
                request.session['password'] = obj.password
                request.session['sex'] = obj.sex
                return redirect('/index/')
        else:
            return render(request, 'login.html', {'obj': obj})


def index(request):
    v = request.session.get('username')
    if not v:
        return redirect('/login/')
    else:
        genge = request.session.get('sex')
        if genge == '男':
            all = models.Woman.objects.all()
            related = models.BtoG.objects.filter(b__username=v).select_related('g')
        else:
            all = models.Man.objects.all()
            related = models.BtoG.objects.filter(g__username=v).select_related('b')
        return render(request, 'index.html', {'username': v, 'all': all, 'related': related, 'genge': genge})


def logout(request):
    request.session.clear()
    return redirect('/login/')
