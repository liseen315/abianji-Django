from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    return render(request, 'index.html', context={
        'title': '我的首页',
        'welcome': '呵呵欢迎'
    })


def page_not_found_view(request,exception,template_name='error.html'):
    if exception:
        logger.error(exception)
    url = request.get_full_path()
    return render(request,template_name,{'message': '哎呀，您访问的地址 ' + url + ' 是一个未知的地方。请点击首页看看别的？', 'statuscode': '404'},status=404)

def server_error_view(request, template_name='error.html'):
    return render(request, template_name,
                  {'message': '哎呀，出错了，我已经收集到了错误信息，之后会抓紧抢修，请点击首页看看别的？', 'statuscode': '500'}, status=500)


def permission_denied_view(request, exception, template_name='error.html'):
    if exception:
        logger.error(exception)
    return render(request, template_name,
                  {'message': '哎呀，您没有权限访问此页面，请点击首页看看别的？', 'statuscode': '403'}, status=403)