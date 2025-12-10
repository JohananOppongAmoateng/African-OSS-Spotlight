from django import forms
from django.forms import ModelForm
from projects.models import Project
from creators.models import Creator


class ProjectForm(ModelForm):
    class Meta:
        fields = ['name', 'about', 'description', 'repository_url', 'tech_stack', 'live_demo_url', 'creator']
        model = Project

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the project name',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'about': forms.TextInput(attrs={
                'placeholder': 'Brief one-line description',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the project, its goals, and what makes it unique.',
                'rows': 4,
                'class': 'form-textarea flex w-full min-w-0 flex-1 resize-y overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 min-h-32 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'repository_url': forms.URLInput(attrs={
                'placeholder': 'https://github.com/user/repo',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'tech_stack': forms.TextInput(attrs={
                'placeholder': 'e.g., React, Node.js, PostgreSQL',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'live_demo_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com (optional)',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'creator': forms.Select(attrs={
                'class': 'form-select flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
        }

        labels = {
            'name': 'Project Name',
            'about': 'Short Description',
            'description': 'Full Description',
            'repository_url': 'Repository Link',
            'tech_stack': 'Tech Stack',
            'live_demo_url': 'Live Demo URL (Optional)',
            'creator': 'Creator',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show verified creators in the dropdown
        self.fields['creator'].queryset = Creator.objects.filter(is_verified=True).order_by('name')