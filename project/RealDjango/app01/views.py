from django.shortcuts import render, redirect, HttpResponse
from app01 import models
from django.views import View


class Login(View):
    def get(self, request):
        get_list = models.Vip.objects.filter(id__gt= 2)
        return render(request, 'login.html', {'get_list': get_list})

    def post(self, request):
        pass


def love(request):
    obj = models.Love.objects.filter(g__nick='胡淑颖').select_related('b')
    for i in obj:
        print(i.b.name)
    ob = models.Boy.objects.filter(name='汪梓成').first()
    p = ob.love_set.all()
    for x in p:
        print(x.g.nick)


def jingdong(request):
    if request.method == 'GET':
        return render(request, 'jingdong.html')
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=user, password=password).first()
        if obj:
            request.session['user'] = obj.username
            request.session['password'] = obj.password
            return redirect('/app01/jd_index/')
        else:
            return render(request, 'jingdong.html', {'message': '密码错误'})


def jd_index(request):
    v = request.session.get('user')
    if v:
        return render(request, 'jd_index.html', {'user': v})
    else:
        return redirect('/app01/jingdong/')

