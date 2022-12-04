import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request=request, template_name='app_1/home.html')


def current_time(request):
    return HttpResponse(f'Current time is {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def workdir(request):
    return HttpResponse(f'{os.listdir(os.path.dirname(os.path.realpath(__file__)))}')
