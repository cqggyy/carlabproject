from django.http import HttpResponse
from django.shortcuts import render
from .models import Manufacturer, Carmodel


# Create your views here.
def index(request):
    manufacturer_list = Manufacturer.objects.all().order_by('id')
    carmodel_list = Carmodel.objects.all().order_by('id')
    return render(request, 'cardb/index.html', context={'manufacturer_list': manufacturer_list, 'carmodel_list': carmodel_list})
