from .models import Setting
from django.conf import settings
from abianji.utils import cache, get_blog_setting

import logging

logger = logging.getLogger(__name__)

'''
seo 处理
'''
def seo_processor(requests):
    key = 'seo_processor'
    value = cache.get(key)
    if value:
        return value
    else:
        logger.info('set processor cache.')
        setting = get_blog_setting()
        value = {
            'SITE_NAME': setting.sitename,
            'SITE_DESCRIPTION': setting.site_description,
            'SITE_KEYWORDS': setting.site_keywords,
            'ARTICLE_SUB_LENGTH': setting.article_sub_length,
            'ANALYTICSCODE': setting.analyticscode
        }
        cache.set(key, value, 60 * 60 * 10)
        return value
