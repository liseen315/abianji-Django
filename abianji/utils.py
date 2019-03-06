from django.core.cache import cache

'''
站点设置
'''
def get_blog_setting():
    value = cache.get('get_blog_setting')
    if value:
        return value
    else:
        from blog.models import Setting
        if not Setting.objects.count():
            setting = Setting()
            setting.sitename = '阿比安吉'
            setting.site_description = 'If you can dream you should do it'
            setting.site_keywords = 'Django blog system'
            setting.article_sub_length = 300
            setting.analyticscode = ''
            setting.save()
        value = Setting.objects.first()
        cache.set('get_blog_setting',value)
        return value