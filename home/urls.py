from django.urls import path
from home.views import home, submission_success

# Create your views here.

urlpatterns = [
    path('', home, name='home'),
    path('success/<str:item_type>/', submission_success, name='submission_success'),
]