import logging
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
class BaseModel(models.Model):
    '''基础模型'''
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField('创建时间',default=now)
    last_mod_time = models.DateTimeField('修改时间',default=now)

    # 需要加上这个抽象Meta字段否则会在数据库内创建对应的表
    class Meta:
        abstract = True

class Setting(BaseModel):
    sitename = models.CharField("网站名称",max_length=100,default='')
    site_description = models.CharField("网站描述",max_length=200,default='')
    site_keywords = models.TextField("网站关键字",max_length=1000,default='')
    article_sub_length = models.IntegerField("文章摘要长度",default=300)
    analyticscode = models.TextField("网站统计代码",max_length=1000,default='')

    class Meta:
        verbose_name = '网站配置'
        # 不写这段就会在网站配置后面多了个s
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if Setting.objects.exclude(id=self.id).count():
            raise ValidationError(_('只能有一个配置'))
