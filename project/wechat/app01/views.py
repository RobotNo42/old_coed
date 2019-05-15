from django.shortcuts import render, HttpResponse, redirect
import time
import requests
import re


def index(request):
    ctime = int(time.time()*1000)
    pathurl = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'.format(ctime)
    ret = requests.get(url=pathurl)
    p = re.findall('uuid = "(.*?)"', ret.text)[0]
    return render(request, 'index.html', {'push': p})
