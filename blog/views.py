from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', context={
        'title': '我的首页',
        'welcome': '呵呵欢迎'
    })
