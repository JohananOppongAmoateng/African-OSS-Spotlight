from django.db import models

# Create your models here.
class Creator(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    bio = models.TextField()
    website_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tech_stack = models.CharField(max_length=500)
    image = models.ImageField(upload_to='creators/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    country = models.CharField(max_length=100)
    skills_and_interests = models.TextField(blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_all_projects(self):
        return self.projects.all()
    
    def projects_count(self):
        return self.projects.count()