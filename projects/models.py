from django.db import models
from creators.models import Creator

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=500)
    description = models.TextField()
    repository_url = models.URLField()
    tech_stack = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    live_demo_url = models.URLField(blank=True, null=True)
    creator = models.ForeignKey(Creator, related_name='projects', on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def creator_name(self):
        return self.creator.name
    