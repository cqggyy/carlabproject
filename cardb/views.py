from django.http import HttpResponse
from django.shortcuts import render
from .models import Manufacturer

# Create your views here.
def index(request):
    manufacturer_list = Manufacturer.objects.all().order_by('id')
    return render(request, 'cardb/index.html', context={'manufacturer_list': manufacturer_list})
