
from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    
    search_fields = ["name"]
    list_display = ["name"]
    
    fieldsets = [("Details", {"fields": ("name", "description")})]


class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ["title", "author"]
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on"]

    fieldsets = [
        ("Details", {"fields": [("title", "entry"), "author", "category"]})]


class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ["entry", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on"]

    fieldsets = [
        ("Details", {"fields": [("entry"), "article", "author"]})]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
