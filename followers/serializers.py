from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError


class FollowerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'author', 'created_at', 'followed', 'followed_name']

    def validate(self, data):
        request = self.context['request']
        followed = data.get('followed')

        if request.user == followed:
            raise serializers.ValidationError(
                {'detail': 'You cannot follow yourself.'}
            )
        return data

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'You are already following this user.'}
            )
