from django.contrib import admin
from .models import Thread, ThreadCategory, Comment


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory
    
    search_fields = ["name"]
    list_display = ["name"]
    
    fieldsets = [("Details", {"fields": ("name", "description")})]


class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    search_fields = ["title", "author"]
    list_display = ["title", "category", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on"]

    fieldsets = [
        ("Details", {"fields": [("title", "entry"), "author", "category"]})]


class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ["thread", "created_on", "updated_on"]
    list_filter = ["created_on", "updated_on"]

    fieldsets = [
        ("Details", {"fields": [("entry"), "thread", "author"]})]


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)