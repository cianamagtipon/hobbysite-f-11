from django.contrib import admin
from .models import Article, ArticleCategory, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "description"]
    fieldsets = [("Details", {"fields": ["name", "description"]})]

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "author", "category", "created_on", "updated_on"]
    list_filter = ["category", "created_on", "updated_on"]
    fieldsets = [("Details", {"fields": ["title", "author", "category", "entry"]})]

class CommentAdmin(admin.ModelAdmin):
    search_fields = ["entry"]
    list_display = ["entry", "author", "article", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on"]

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
