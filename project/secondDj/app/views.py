from django.shortcuts import render,redirect,HttpResponse
import json


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        passwd = request.POST.get('passwd')
        if user == 'chengge1124' and passwd == "123456":
            return redirect("http://baidu.com")
        else:
            return render(request, "login.html", {'msg': '用户名或者密码错误'})