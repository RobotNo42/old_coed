from django.shortcuts import render, HttpResponse, redirect
import time
import requests
import re
from django.http import JsonResponse
from bs4 import BeautifulSoup


# 将xml变成字典形式
def xml_parse(text):
    result = {}
    soup = BeautifulSoup(text, features='html.parser')
    tag_list = soup.find(name='error').find_all()
    for i in tag_list:
        result[i.name] = i.text
    return result


# 首页
def index(request):
    ctime = int(time.time()*1000)
    pathurl = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'.format(ctime)
    ret = requests.get(url=pathurl)
    p = re.findall('uuid = "(.*?)"', ret.text)[0]
    request.session['p'] = p
    return render(request, 'index.html', {'push': p})


# 登录校验
def check_login(request):
    ret = {'code': 408, 'pic': '', 'begin_url': ''}
    p = request.session['p']
    ctime = int(time.time() * 1000)
    purl = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=1&r=1094968425&_={1}'.format(p,ctime)
    rep = requests.get(url=purl,
                       headers={
                           'Referer': 'https://wx.qq.com/',
                           'Host': 'login.wx.qq.com',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400'
                       }
                       )
    # 说明没有扫码或者失败
    if 'window.code=408' in rep.text:
        pass
    # 扫码成功
    elif 'window.code=201' in rep.text:
        pic = re.findall("window.userAvatar = '(.*?)';", rep.text)[0]
        ret['code'] = 201
        ret['pic'] = pic
    # 手机上确认登录
    elif 'window.code=200' in rep.text:
        ret['code'] = 200
        ret['begin_url'] = re.findall('window.redirect_uri="(.*)"', rep.text)[0] + '&fun=new&version=v2'
        ru = requests.get(ret['begin_url'])
        print(ru.text)
        tick_dict = xml_parse(ru.text)
        request.session['tick'] = tick_dict
        request.session['ticks'] = ru.cookies.get_dict()
    return JsonResponse(ret)


def wechat(request):
    pass_ticket = request.session['tick']['pass_ticket']
    init_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=818473596&pass_ticket={0}'.format(pass_ticket)
    rep = requests.post(url=init_url,
                        json={
                            'BaseRequest': {
                                'DeviceID': 'e384106504168856',
                                'Sid': request.session['tick']['wxsid'],
                                'Skey': request.session['tick']['skey'],
                                'Uin': request.session['tick']['wxuin']
                            }
                        }

                        )
    rep.encoding = 'utf-8'
    init_user_dict = rep.json()
    return render(request, 'wechat.html', {'dict': init_user_dict})


# 获取微信联系人
def all_user(request):
    pass_ticket = request.session['tick']['pass_ticket']
    skey = request.session['tick']['skey']
    ctime = int(time.time()*1000)
    all_user_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?pass_ticket={0}&r={1}&seq=0&skey={2}'.format(pass_ticket, ctime, skey)
    reg = requests.get(url=all_user_url,
                       headers={
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
                           'Referer': 'https://wx.qq.com/',
                           'Host': 'wx.qq.com',
                           'Connection': 'keep-alive',
                           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                           'Accept-Encoding': 'gzip, deflate, br',

                       },
                       cookies=request.session['ticks']
                       )
    reg.encoding = 'utf-8'
    all_user_dict = reg.json()
    return render(request, 'all_user.html', {'all_user': all_user_dict})


# 获取微信联系人头像
def get_img(request):
    pre = request.GET.get('pev')
    username = request.GET.get('username')
    skey = request.GET.get('skey')
    get_img_url = 'https://wx.qq.com{0}&username={1}&skey={2}'.format(pre, username, skey)
    reg = requests.get(url=get_img_url,
                       cookies=request.session['ticks']
                       )
    return HttpResponse(reg.content)


# 发送消息
def send_msg(request):
    if request.method == 'GET':
        return render(request, 'msg.html')
    else:
        pass_ticket = request.session['tick']['pass_ticket']
        send_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}'.format(pass_ticket)
        ctime = int(time.time() * 1000)
        rep = requests.post(url=send_url,
                            json={
                                'BaseRequest': {
                                    'DeviceID': 'e682222205573003',
                                    'Sid': request.session['tick']['wxsid'],
                                    'Skey': request.session['tick']['skey'],
                                    'Uin': request.session['tick']['wxuin']
                                },
                                'Msg': {
                                    'ClientMsgId': ctime,
                                    'Content': '',

                                }
                            }
                            )
        return
