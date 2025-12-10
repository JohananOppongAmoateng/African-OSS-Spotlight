from django.urls import path
from projects import views

urlpatterns = [
    path('', views.explore_projects, name='explore-projects'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('submit/', views.submit_project, name='submit-project'),
]