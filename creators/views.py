from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from creators.models import Creator
from creators.forms import CreatorForm, ProjectFormSet
from django.core.paginator import Paginator

# Create your views here.
def explore_creators(request):
    # Get search query from request
    search_query = request.GET.get('q', '')
    
    # Start with verified creators
    creators = Creator.objects.filter(is_verified=True)
    
    # Apply search filter if query exists
    if search_query:
        creators = creators.filter(
            Q(name__icontains=search_query) |
            Q(bio__icontains=search_query) |
            Q(country__icontains=search_query) |
            Q(skills_and_interests__icontains=search_query) |
            Q(job_title__icontains=search_query)
        )
    
    creators = creators.order_by('-created_at')
    paginator = Paginator(creators, 20)  # Show 20 creators per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'creators/explore-creators.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })

def creator_detail(request, creator_id):
    creator = get_object_or_404(Creator, id=creator_id)
    # Split skills and tech stacks for template display
    if creator.skills_and_interests:
        creator.skills_list = [s.strip() for s in creator.skills_and_interests.split(',')]
    else:
        creator.skills_list = []
    
    if creator.tech_stack:
        creator.tech_list = [t.strip() for t in creator.tech_stack.split(',')]
    else:
        creator.tech_list = []
    
    # Add tech list for each project
    for project in creator.projects.all():
        if project.tech_stack:
            project.tech_list = [t.strip() for t in project.tech_stack.split(',')]
        else:
            project.tech_list = []
    
    return render(request, 'creators/creator-profile.html', {'creator': creator})

def submit_creator(request):
    if request.method == 'POST':
        form = CreatorForm(request.POST, request.FILES)
        formset = ProjectFormSet(request.POST, instance=Creator())
        
        if form.is_valid() and formset.is_valid():
            creator = form.save(commit=False)
            creator.is_verified = False  # Requires admin verification
            creator.save()
            
            # Save the projects associated with this creator
            formset.instance = creator
            projects = formset.save(commit=False)
            for project in projects:
                project.is_verified = False  # Projects also need verification
                project.save()
            
            messages.success(
                request,
                f'Creator "{creator.name}" and {len(projects)} project(s) nominated successfully! They will appear publicly after admin verification.'
            )
            return redirect('submission_success', item_type='creator')
    else:
        form = CreatorForm()
        formset = ProjectFormSet(instance=Creator())
    
    return render(request, 'creators/submit-creator.html', {
        'form': form,
        'formset': formset,
    })