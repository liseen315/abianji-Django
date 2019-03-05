from django.contrib import admin
from .models import Category,Article,ArticleType,Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(ArticleType)

