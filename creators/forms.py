from django import forms
from django.forms import ModelForm, inlineformset_factory
from creators.models import Creator
from projects.models import Project


class CreatorForm(ModelForm):
    class Meta:
        fields = ['name', 'job_title', 'bio', 'country', 'skills_and_interests', 'website_url', 'image']
        model = Creator

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Ada Lovelace',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'job_title': forms.TextInput(attrs={
                'placeholder': 'e.g. Software Engineer',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': 'Tell us a little about the creator...',
                'rows': 4,
                'class': 'form-textarea flex w-full min-w-0 flex-1 resize-y overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 min-h-32 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'e.g. Nigeria',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'skills_and_interests': forms.Textarea(attrs={
                'placeholder': 'e.g. JavaScript, Python, UI/UX (comma separated)',
                'rows': 3,
                'class': 'form-textarea flex w-full min-w-0 flex-1 resize-y overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'website_url': forms.URLInput(attrs={
                'placeholder': 'https://example.com',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-14 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 placeholder:text-text-subtle p-[15px] text-base font-normal leading-normal'
            }),
        }

        labels = {
            'name': 'Full Name',
            'job_title': 'Job Title',
            'bio': 'Bio',
            'country': 'Country',
            'skills_and_interests': 'Skills & Interests',
            'website_url': 'Website URL',
            'image': 'Profile Photo',
        }


# Inline formset for adding projects when creating a creator
ProjectFormSet = inlineformset_factory(
    Creator,
    Project,
    fields=['name', 'about', 'description', 'repository_url', 'tech_stack', 'live_demo_url'],
    extra=2,  # Allow adding up to 2 projects initially
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={
            'placeholder': 'Project name',
            'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-12 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
        'about': forms.TextInput(attrs={
            'placeholder': 'Brief description',
            'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-12 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
        'description': forms.Textarea(attrs={
            'placeholder': 'Full description',
            'rows': 3,
            'class': 'form-textarea flex w-full min-w-0 flex-1 resize-y overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
        'repository_url': forms.URLInput(attrs={
            'placeholder': 'https://github.com/user/repo',
            'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-12 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
        'tech_stack': forms.TextInput(attrs={
            'placeholder': 'e.g., React, Node.js',
            'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-12 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
        'live_demo_url': forms.URLInput(attrs={
            'placeholder': 'https://demo.com (optional)',
            'class': 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg text-text-main dark:text-background-light focus:outline-0 focus:ring-2 focus:ring-panafrican-yellow/50 border border-border-color dark:border-panafrican-black/50 bg-white dark:bg-panafrican-black/30 h-12 placeholder:text-text-subtle p-[12px] text-sm font-normal leading-normal'
        }),
    }
)