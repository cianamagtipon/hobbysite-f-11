from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

    search_fields=['name']
    list_display=['name']

    fieldsets = [("Details", {"fields": ("name", "description")})]


class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = [
        "title",
    ]
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on",]

    fieldsets =[("Details", {"fields": [("title", "entry"), "category"]})]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

