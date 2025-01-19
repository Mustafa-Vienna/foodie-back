from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  author = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200, blank=True)
  content = models.TextField(blank=True)
  image = models.ImageField(
    upload_to='images/', default='../default_profile_girwrs'
  )
  
  class Meta:
    ordering = ['-created_at']
    
  def __str__(self):
      return f"{self.author}'s profile"
  

def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(author=instance)

post_save.connect(create_profile, sender=User)