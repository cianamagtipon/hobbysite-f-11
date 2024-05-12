from django.contrib import admin
from .models import Commission, Job, JobApplication


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    search_fields = ['title', 'description']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['commission', 'role', 'manpower_required', 'status']
    list_filter = ['status', 'role']
    search_fields = ['role', 'commission__title']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'status', 'applied_on']
    list_filter = ['status', 'applied_on']
    search_fields = ['job__role', 'applicant__username']
