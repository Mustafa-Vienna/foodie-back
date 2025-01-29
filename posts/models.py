from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
  """
  Tag model for categorizing posts
  """
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
    verbose_name_plural = "Tags"
  
  def __str__(self):
    return self.name
  

class Post(models.Model):
  """
  Post model, linked to an author with various attributes
  Including category, tags, image and filter option.
  """
  CATEGORY_CHOICES = [
    ('seafood', 'Seafood'),
    ('vegetarian', 'Vegetarian'),
    ('cold', 'Cold Dishes'),
    ('warm', 'Warm Dishes'),
    ('desert', 'Desert'),
    ('others', 'Others'),
  ]
  
  IMAGE_FILTER_CHOICES = [
    ('vintage', 'Vintage'),
    ('black_and_white', 'Black & White'),
    ('sepia', 'Sepia'),
    ('contrast', 'High Contrast'),
    ('bright', 'Bright'),
    ('normal', 'Normal'),
  ]

  
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='posts', verbose_name='Post Author'
    )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=250)
  content = models.TextField(blank=True)
  image = models.ImageField(
    upload_to='images/', default='../default_post_f3ugv9', blank=True
  )
  category = models.CharField(max_length=60, choices=CATEGORY_CHOICES, default='others')
  tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
  image_filter = models.CharField(
    max_length = 20, choices=IMAGE_FILTER_CHOICES, default='normal'
  )

  
  class Meta:
    ordering = ['-created_at']
    verbose_name_plural = "Posts"
    
  def __str__(self):
    return f"{self.author.username}'s Post - {self.title}"
  