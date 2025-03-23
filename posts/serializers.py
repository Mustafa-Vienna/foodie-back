from rest_framework import serializers
from posts.models import Post, Tag
from likes.models import Like
from cloudinary.utils import cloudinary_url

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(source='author.profile.image.url')
    category = serializers.ChoiceField(choices=Post.CATEGORY_CHOICES, default='others')
    image_filter = serializers.ChoiceField(choices=Post.IMAGE_FILTER_CHOICES, default='normal')
    
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Tag.objects.all(),
        source='tags',
        required=False,
    )
    
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    image = serializers.ImageField(required=False, allow_null=True)

    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        return "https://res.cloudinary.com/duemxeswe/image/upload/v1737306345/default_post_f3ugv9.jpg"

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(author=user, post=obj).first()
            return like.id if like else None
        return None

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def validate_image(self, value):
        if value and value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size cannot exceed 2MB.")
        if value and (value.image.height > 4096 or value.image.width > 4096):
            raise serializers.ValidationError("Image dimensions cannot exceed 4096x4096px.")
        return value
    
    def validate_content(self, value):
        required_keys = ["introduction", "ingredients", "steps", "conclusion"]
        if not all(key in value for key in required_keys):
            raise serializers.ValidationError("Content must include introduction, ingredients, steps, and conclusion.")
        return value

    def validate_title(self, value):
        if len(value) > 250:
            raise serializers.ValidationError("Title cannot exceed 250 characters.")
        return value

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
        instance.image_filter = validated_data.get('image_filter', instance.image_filter)
        instance.save()
        if tags_data:
            instance.tags.set(tags_data)
        return instance

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'category', 'tags', 'tag_ids',
            'image_filter', 'like_id', 'likes_count', 'comments_count'
        ]