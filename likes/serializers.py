from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'author', 'post']

    def validate(self, data):
        author = self.context['request'].user
        post = data.get('post')

        if Like.objects.filter(author=author, post=post).exists():
            raise serializers.ValidationError(
                "You have already liked this post."
                )
        return data
