from django.contrib import admin

# Register your models here.
# 超级管理员增加和删除
from article.models import Article

admin.site.register(Article)