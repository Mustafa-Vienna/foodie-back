from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source = 'author.username')
  
  class Meta:
    model = Profile
    fields = [
      'id', 'author', 'created_at', 'updated_at', 'name',
      'content', 'image'
    ]