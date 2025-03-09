from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
    user = self.user
    
    profile_image = user.profile.image if hasattr(user, "profile") and user.profile.image else None
    
    # If profile_image is a full URL, return as is; otherwise, append Cloudinary base URL
    if profile_image:
      profile_image_url = profile_image.url if hasattr(profile_image, "url") else (
          profile_image if profile_image.startswith("http") else f"https://res.cloudinary.com/duemxeswe/image/upload/{profile_image}"
      )
    else:
      profile_image_url = "https://res.cloudinary.com/duemxeswe/image/upload/v1737306346/default_profile_girwrs.jpg"
            
    data["user"] = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "profile_id": user.profile.id if hasattr(user, "profile") else None,
        "profile_image": profile_image_url,
    }
    return data

class ProfileSerializer(serializers.ModelSerializer):
  """
  Serializer for the Profile model
  Adds extra fields for ownership and follow-related data.
  """
  author = serializers.ReadOnlyField(source = 'author.username')
  is_author = serializers.SerializerMethodField()
  following_id = serializers.SerializerMethodField()
  followers_count = serializers.SerializerMethodField()
  following_count = serializers.SerializerMethodField()
  posts_count = serializers.SerializerMethodField()
  image = serializers.SerializerMethodField()
  
  def get_image(self, obj):
    """
    Ensure Cloudinary returns a full URL for the profile image.
    """
    if obj.image:
      if isinstance(obj.image, str) and obj.image.startswith("http"):
          return obj.image
      if hasattr(obj.image, "url"):
          return obj.image.url
      return f"https://res.cloudinary.com/duemxeswe/image/upload/{obj.image}"

    return "https://res.cloudinary.com/duemxeswe/image/upload/v1737306346/default_profile_girwrs.jpg"
  
  def get_is_author(self, obj):
    request = self.context['request']
    return request.user == obj.author
  
  def get_following_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
      following = Follower.objects.filter(
        author=user, followed=obj.author
      ).first()
      return following.id if following else None
    return None
  
  def get_followers_count(self, obj):
    return Follower.objects.filter(followed=obj.author).count()
  
  def get_following_count(self, obj):
    return Follower.objects.filter(author=obj.author).count()
  
  def get_posts_count(self, obj):
    return obj.author.posts.count()
  
  class Meta:
    model = Profile
    fields = [
      'id', 'author', 'created_at', 'updated_at', 'name',
      'content', 'image', 'is_author', 'following_id',
      'followers_count', 'following_count', 'posts_count'
    ]