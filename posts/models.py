from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
  TAG_CHOICES = [
    ('spicy', 'Spicy'),
    ('sweet', 'Sweet'),
    ('savory', 'Savory'),
    ('bitter', 'Bitter'),
    ('sour', 'Sour'),
    ('salty', 'Salty'),
    ('umami', 'Umami'),
    ('others', 'Others'),
  ]
  
  name = models.CharField(
    max_length=60, choices=TAG_CHOICES, default='others'
    )
  
  class Meta:
    ordering = ['name']
  
  def __str__(self):
    return self.get_name_display()
  

class Post(models.Model):
  CATEGORY_CHOICES = [
    ('seafood', 'Seafood'),
    ('vegetarian', 'Vegetarian'),
    ('cold', 'Cold Dishes'),
    ('warm', 'Warm Dishes'),
    ('desert', 'Desert'),
    ('others', 'Others'),
  ]
  
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='posts', verbose_name='Post Author')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=250)
  content = models.TextField(blank=True)
  image = models.ImageField(
    upload_to='images/', default='../default_post_f3ugv9', blank=True
  )
  category = models.CharField(max_length=60, choices=CATEGORY_CHOICES, default='others')
  tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

  
  class Meta:
    ordering = ['-created_at']
    
  def __str__(self):
    return f"{self.id} {self.title}"
  