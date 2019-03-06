from django.contrib import admin

from .models import Setting,Article,Category,Tag

class ArticleAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class BlogSettingAdmin(admin.ModelAdmin):
    pass