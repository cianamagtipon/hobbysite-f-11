from django.contrib import admin
from .models import Commission, Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    
    search_fields = ["title"]
    list_display = ["title", "created_on", "updated_on"]
    
    fieldsets = [("Details", {"fields": [("title", "description"), "people_required"]})]


class CommentAdmin(admin.ModelAdmin):
    model = Comment

    search_fields = ["commission"]
    list_display = ["created_on"]
    list_filter = ["created_on", "updated_on"]

    fieldsets = [
        ("Details", {"fields": [("entry"), "commission"]})]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)