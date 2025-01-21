from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=250)
  content = models.TextField(blank=True)
  image = models.ImageField(
    upload_to='images/', default='../default_profile_girwrs', blank=True
  )
  
  class Meta:
    ordering = ['-created_at']
    
  def __str__(self):
    return f"{self.id} {self.title}"