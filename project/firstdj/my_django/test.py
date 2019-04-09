from django.shortcuts import HttpResponse, render, redirect
from utils import sqlfirst
import json


def work(request):
    student = sqlfirst.get_list('select id,name from student', [])
    return render(request, 'work.html', {'student': student})
