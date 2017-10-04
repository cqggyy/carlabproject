from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'cardb/index.html', context={
                    'title': '汽车Lab',
                    'welcome': '欢迎访问汽车实验室CarLab首页！'
            })
