from django.http import HttpResponse
from django.shortcuts import render
from .models import Carmaker, Carmodel

from django.contrib.auth.decorators import login_required#登陆后才能进入系统的模块
@login_required  #登陆后才能进入系统


# Create your views here.
def index(request):
    manufacturer_list = Carmaker.objects.all().order_by('id')
    carmodel_list = Carmodel.objects.all().order_by('id')
    return render(request, 'cardb/index.html', context={'manufacturer_list': manufacturer_list, 'carmodel_list': carmodel_list})
