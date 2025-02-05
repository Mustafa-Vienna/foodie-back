from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class CurrentUserSerializer(UserDetailsSerializer):
  profile_id = serializers.ReadOnlyField(source='profile.id')
  profile_image = serializers.ReadOnlyField(source='profile.image.url')
  
  class Meta(UserDetailsSerializer):
    fields = UserDetailsSerializer.Meta.fields + (
      'profile_id', 'profile_image'
    )
    
class CustomRegisterSerializer(RegisterSerializer):
  email = serializers.EmailField(
    required=True,
    max_length=80,
    error_messages={
      "required": "Email is required",
      "invalid": "Enter a valid email address!",
      "max_length": "Email must be less then 80 characters!",
    },
  )
  
  def validate_email(self, value):
    """
    Ensure that the email is unique
    """
    
    email = value.strip().lower()
    
    if User.objects.filter(email=email).exists():
      raise serializers.ValidationError("A user with this email already exists.")
    
    return email
  
  def save(self, request):
    """
    Save the user with email
    """
    user = super().save(request)
    setup_user_email(request, user, [])
    return user