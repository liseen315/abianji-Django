import logging
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    '''基础模型'''
    id = models.AutoField(primary_key=True)
    # create_time = models.DateTimeField('创建时间', default=now)
    # last_mod_time = models.DateTimeField('修改时间', default=now)

    # 需要加上这个抽象Meta字段否则会在数据库内创建对应的表
    class Meta:
        abstract = True


class Setting(BaseModel):
    sitename = models.CharField("网站名称", max_length=100, default='')
    site_description = models.CharField("网站描述", max_length=200, default='')
    site_keywords = models.TextField("网站关键字", max_length=1000, default='')
    article_sub_length = models.IntegerField("文章摘要长度", default=300)
    analyticscode = models.TextField("网站统计代码", max_length=1000, default='')

    class Meta:
        verbose_name = '网站配置'
        # 不写这段就会在网站配置后面多了个s
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if Setting.objects.exclude(id=self.id).count():
            raise ValidationError(_('只能有一个配置'))

    # 覆盖父类方法当在admin保存新的设置的时候清空缓存
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from abianji.utils import cache
        cache.clear()


class Category(BaseModel):
    name = models.CharField('分类名', max_length=30, unique=True)

    class Meta:
        # 默认以name排序
        ordering = ['name']
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField('标签', max_length=30, unique=True)

    class Meta:
        # 默认以name排序
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    TYPE = (
        ('article', '文章类'),
        ('audio', '音频类'),
        ('code', '代码类'),
        ('gallery', '图文类'),
        ('link', '引用类')
    )
    title = models.CharField('标题',max_length=200,unique=True)
    body = models.TextField('正文')
    pub_time = models.DateTimeField('发布时间',blank=True,null=True)
    article_type = models.CharField('类型',max_length=10,choices=TYPE,default='article')
    views = models.PositiveIntegerField('浏览量',default=0)
    category = models.ForeignKey('Category',verbose_name='分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',verbose_name='标签',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
