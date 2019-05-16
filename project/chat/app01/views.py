from django.shortcuts import render, HttpResponse, redirect
import time
import requests
import re
from django.http import JsonResponse
from bs4 import BeautifulSoup


def index(request):
    ctime = int(time.time()*1000)
    pathurl = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'.format(ctime)
    ret = requests.get(url=pathurl)
    p = re.findall('uuid = "(.*?)"', ret.text)[0]
    request.session['p'] = p
    return render(request, 'index.html', {'push': p})


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
        tick_dict = xml_parse(ru.text)
        request.session['tick'] = tick_dict
    return JsonResponse(ret)


def xml_parse(text):
    result = {}
    soup = BeautifulSoup(text, features='html.parser')
    tag_list = soup.find(name='error').find_all()
    for i in tag_list:
        result[i.name] = i.text
    return result
