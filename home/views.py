from django.shortcuts import render
from creators.models import Creator
from projects.models import Project

# Create your views here.
def home(request):
    creators = Creator.objects.filter(is_verified=True).order_by('?')[:3]
    projects = Project.objects.filter(is_verified=True).order_by('?')[:3]
    return render(request, 'home/home.html', {'creators': creators, 'projects': projects})

def submission_success(request, item_type):
    """Generic success page for creator/project submissions"""
    return render(request, 'submission-success.html', {'item_type': item_type})