from django.shortcuts import render,HttpResponse,redirect
from webapp01 import models
from django.forms import Form
from django.forms import fields
from django.http import JsonResponse
from geetest import GeetestLib


class MyForm(Form):
    username = fields.CharField(required=True, error_messages={
        'required': '用户名不能为空'
    })
    password = fields.CharField(required=True, error_messages={
     'required': '密码不能为空'
    })


def login(request):
    if request.method == 'POST':
        ret = {"status": 0, "msg": "", "obj": ""}
        username = request.POST.get('username')
        password = request.POST.get('password')
        sex = request.POST.get('sex')
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        obj = MyForm(request.POST)
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            if obj.is_valid():
                if sex == '男':
                    obj = models.Man.objects.filter(username=username, password=password).first()
                else:
                    obj = models.Woman.objects.filter(username=username, password=password).first()
                if not obj:
                    # 用户名密码错误
                    ret["status"] = 1
                    ret["msg"] = "用户名或密码错误！"
                else:
                    request.session['username'] = obj.username
                    request.session['password'] = obj.password
                    request.session['sex'] = obj.sex
                    ret["msg"] = "/index/"
            else:
                ret["status"] = 1
                ret["obj"] = obj.errors
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)
    return render(request, 'login.html')


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


pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)
