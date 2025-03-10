from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
  """
  The profile model linked to a User, and
  it will actomatically created when a User is created
  """
  author = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200, blank=True)
  content = models.TextField(blank=True)
  image = CloudinaryField(
    'images', default='v1737306346/default_profile_girwrs.jpg'
  )
  
  class Meta:
    ordering = ['-created_at']
    
  def __str__(self):
      return f"{self.author.username}'s profile"
  

def create_profile(sender, instance, created, **kwargs):
  """
  Create a Profile instance for each new User
  """
  if created:
    Profile.objects.create(author=instance)

post_save.connect(create_profile, sender=User)