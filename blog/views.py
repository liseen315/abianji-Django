from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, Category, Tag
import logging

logger = logging.getLogger(__name__)


# Create your views here.

class ArticleListView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'blog/article_list.html'

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article_list'

    # 子类覆盖方法用于获取文章列表
    def get_articalListData(self):
        pass

    def get_queryset(self):
        value = self.get_articalListData()
        return value

"""
首页视图
"""
class IndexView(ArticleListView):

    def get_articalListData(self):
        article_list = Article.objects.all()
        return article_list

"""
文章详情
"""
class ArticleDetailView(DetailView):
    pass

def page_not_found_view(request, exception, template_name='error.html'):
    if exception:
        logger.error(exception)
    url = request.get_full_path()
    return render(request, template_name, {'message': '哎呀，您访问的地址 ' + url + ' 是一个未知的地方。请点击首页看看别的？', 'statuscode': '404'},
                  status=404)


def server_error_view(request, template_name='error.html'):
    return render(request, template_name,
                  {'message': '哎呀，出错了，我已经收集到了错误信息，之后会抓紧抢修，请点击首页看看别的？', 'statuscode': '500'}, status=500)


def permission_denied_view(request, exception, template_name='error.html'):
    if exception:
        logger.error(exception)
    return render(request, template_name,
                  {'message': '哎呀，您没有权限访问此页面，请点击首页看看别的？', 'statuscode': '403'}, status=403)
