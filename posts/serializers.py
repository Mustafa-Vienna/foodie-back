from rest_framework import serializers
from posts.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
  name = serializers.ChoiceField(choices=Tag.TAG_CHOICES)
  
  class Meta:
    model = Tag
    fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
  author = serializers.ReadOnlyField(source = 'author.username')
  is_author = serializers.SerializerMethodField()
  profile_id = serializers.ReadOnlyField(source = 'author.profile.id')
  profile_image = serializers.ReadOnlyField(source = 'author.profile.image.url')
  category = serializers.ChoiceField(choices=Post.CATEGORY_CHOICES, default='others')
  tags = serializers.PrimaryKeyRelatedField(
    many=True,
    queryset = Tag.objects.all(),
    required = False,
    )
  
  
  class Meta:
    model = Post
    fields = [
      'id', 'author', 'is_author', 'profile_id',
      'profile_image', 'created_at', 'updated_at',
      'title', 'content', 'image', 'category', 'tags'
    ]
    
  def get_is_author(self, obj):
    request = self.context['request']
    return request.user == obj.author
  
  
  def create(self, validated_data):
    tags_data = validated_data.pop('tags', [])
    post = Post.objects.create(**validated_data)
    
    for tag in tags_data:
      post.tags.add(tag)
    
    return post
  
  def update(self, instance, validated_data):
    tags_data = validated_data.pop('tags', [])
    instance.title = validated_data.get('title', instance.title)
    instance.content = validated_data.get('content', instance.content)
    instance.category = validated_data.get('category', instance.category)
    instance.image = validated_data.get('image', instance.image)
    instance.save()
    
    if tags_data:
        instance.tags.set(tags_data)
      
    return instance
  
 