import logging
from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings

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
