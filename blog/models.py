from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    ARTICLE_TYPE = 'ARTICLE'
    AUDIO_TYPE = 'AUDIO'
    CODE_TYPE = 'CODE'
    GALLERY_TYPE = 'GALLERY'
    VIDEO_TYPE = 'VIDEO'
    ARTICLE_TYPE_CHOICES = (
        (ARTICLE_TYPE, 'article'),
        (AUDIO_TYPE, 'audio'),
        (CODE_TYPE, 'code'),
        (GALLERY_TYPE, 'gallery'),
        (VIDEO_TYPE, 'video')
    )
    name = models.CharField(max_length=10, choices=ARTICLE_TYPE_CHOICES, default=ARTICLE_TYPE)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.OneToOneField(ArticleType,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
