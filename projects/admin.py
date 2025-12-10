from django.contrib import admin
from projects.models import Project

# Register your models here.


@admin.action(description='Verify selected projects')
def verify_projects(modeladmin, request, queryset):
    """Bulk action to verify projects"""
    updated = queryset.update(is_verified=True)
    modeladmin.message_user(request, f'{updated} project(s) successfully verified.')


@admin.action(description='Unverify selected projects')
def unverify_projects(modeladmin, request, queryset):
    """Bulk action to unverify projects"""
    updated = queryset.update(is_verified=False)
    modeladmin.message_user(request, f'{updated} project(s) marked as unverified.')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'is_verified', 'created_at', 'updated_at')
    list_filter = ('is_verified', 'created_at', 'updated_at', 'creator')
    search_fields = ('name', 'description', 'tech_stack', 'creator__name')
    ordering = ('-created_at',)
    actions = [verify_projects, unverify_projects]
    
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'creator', 'about')
        }),
        ('Details', {
            'fields': ('description', 'tech_stack')
        }),
        ('Links', {
            'fields': ('repository_url', 'live_demo_url')
        }),
        ('Verification & Dates', {
            'fields': ('is_verified', 'created_at', 'updated_at')
        }),
    )
    
    # Allow filtering by creator in the admin
    autocomplete_fields = []


admin.site.register(Project, ProjectAdmin)