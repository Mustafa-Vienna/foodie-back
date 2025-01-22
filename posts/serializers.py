from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source = 'author.username')
  is_author = serializers.SerializerMethodField()
  profile_id = serializers.ReadOnlyField(source = 'author.profile.id')
  profile_image = serializers.ReadOnlyField(source = 'author.profile.image.url')
  
  def get_is_author(self, obj):
    request = self.context['request']
    return request.user == obj.author
  
  class Meta:
    model = Post
    fields = [
      'id', 'author', 'is_author', 'profile_id',
      'profile_image', 'created_at', 'updated_at',
      'title', 'content', 'image', 'category',
    ]