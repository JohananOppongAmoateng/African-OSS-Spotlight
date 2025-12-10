from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from projects.models import Project
from projects.forms import ProjectForm
from django.core.paginator import Paginator


def explore_projects(request):
    # Get search query from request
    search_query = request.GET.get('q', '')
    
    # Start with verified projects
    projects = Project.objects.filter(is_verified=True)
    
    # Apply search filter if query exists
    if search_query:
        projects = projects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(about__icontains=search_query) |
            Q(tech_stack__icontains=search_query) |
            Q(creator__name__icontains=search_query)
        )
    
    projects = projects.order_by('-created_at')
    paginator = Paginator(projects, 20)  # Show 20 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'projects/explore-projects.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Parse tech stack into a list for better display
    if project.tech_stack:
        project.tech_list = [t.strip() for t in project.tech_stack.split(',')]
    else:
        project.tech_list = []
    
    return render(request, 'projects/project-detail.html', {'project': project})


def submit_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.is_verified = False  # Requires admin verification
            project.save()
            messages.success(
                request, 
                f'Project "{project.name}" submitted successfully! It will appear publicly after admin verification.'
            )
            return redirect('submission_success', item_type='project')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/submit-project.html', {'form': form})