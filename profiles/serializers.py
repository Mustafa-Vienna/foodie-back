from rest_framework import serializers
from .models import Profile
from followers.models import Follower

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