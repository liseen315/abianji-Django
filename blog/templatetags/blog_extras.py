import logging
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.urls import reverse

logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def datetimeformat(value):
    """
    格式化日期
    :param value:
    :return:
    """
    try:
        return value.strftime(settings.DATE_TIME_FORMAT)
    except Exception as e:
        logger.error(e)
        return ""


@register.filter(is_safe=True)
@stringfilter
def truncatechars_content(content):
    """
    文章摘要
    :param content:
    :return:
    """
    from django.template.defaultfilters import truncatechars_html
    from abianji.utils import get_blog_setting
    blogsetting = get_blog_setting()
    return truncatechars_html(content, blogsetting.article_sub_length)


@register.inclusion_tag('blog/tags/article_bytype.html')
def load_article_byType(article, isindex):
    """
    根据类型加载模板并且传递参数
    :param article:
    :param isindex:
    :return:
    """
    return {
        'article': article,
        'isindex': isindex
    }


@register.inclusion_tag('blog/tags/pageination.html')
def load_pagination_info(page_obj):
    """
    分页
    :param page_obj:
    :return:
    """
    previous_url = ''
    next_url = ''
    if page_obj.has_next():
        next_number = page_obj.next_page_number()
        next_url = reverse('blog:index_page', kwargs={'page': next_number})
    if page_obj.has_previous():
        previous_number = page_obj.previous_page_number()
        previous_url = reverse('blog:index_page', kwargs={'page': previous_number})

    return {
        'previous_url': previous_url,
        'next_url': next_url,
        'page_obj': page_obj
    }
