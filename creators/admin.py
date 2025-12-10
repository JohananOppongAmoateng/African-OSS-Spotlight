from django.contrib import admin
from creators.models import Creator

# Register your models here.


@admin.action(description='Verify selected creators')
def verify_creators(modeladmin, request, queryset):
    """Bulk action to verify creators"""
    updated = queryset.update(is_verified=True)
    modeladmin.message_user(request, f'{updated} creator(s) successfully verified.')


@admin.action(description='Unverify selected creators')
def unverify_creators(modeladmin, request, queryset):
    """Bulk action to unverify creators"""
    updated = queryset.update(is_verified=False)
    modeladmin.message_user(request, f'{updated} creator(s) marked as unverified.')


class CreatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'job_title', 'is_verified', 'created_at', 'projects_count')
    list_filter = ('is_verified', 'country', 'created_at')
    search_fields = ('name', 'bio', 'tech_stack', 'country', 'skills_and_interests')
    ordering = ('-created_at',)
    actions = [verify_creators, unverify_creators]
    
    readonly_fields = ('created_at', 'followers_count')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'job_title', 'country', 'image')
        }),
        ('About', {
            'fields': ('bio', 'skills_and_interests', 'tech_stack')
        }),
        ('Links', {
            'fields': ('website_url', 'social_links')
        }),
        ('Verification', {
            'fields': ('is_verified', 'created_at', 'followers_count')
        }),
    )
    
    def projects_count(self, obj):
        """Display number of projects"""
        return obj.projects.count()
    projects_count.short_description = 'Projects'


admin.site.register(Creator, CreatorAdmin)