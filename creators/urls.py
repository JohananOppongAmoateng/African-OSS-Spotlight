from django.urls import path
from creators import views

urlpatterns = [
    path('', views.explore_creators, name='explore-creators'),
    path('<int:creator_id>/', views.creator_detail, name='creator_detail'),
    path('nominate/', views.submit_creator, name='submit-creator'),
]