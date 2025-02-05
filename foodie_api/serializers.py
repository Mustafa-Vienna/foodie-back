from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer


class CurrentUserSerializer(UserDetailsSerializer):
  profile_id = serializers.ReadOnlyField(source='profile.id')
  profile_image = serializers.ReadOnlyField(source='profile.image.url')
  
  class Meta(UserDetailsSerializer):
    fields = UserDetailsSerializer.Meta.fields + (
      'profile_id', 'profile_image'
    )
    
  class CustomeRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    
    def validate_email(self, email):
      
      email = get_adapter.clean_email(email)
      if email and self.Meta.model.objects.filter(email=email).exist():
        raise serializers.ValidationError("A user with this email already exists.")
      return email
    
  def save(self, request):
    user = super().save(request)
    setup_user_email(request, user, [])
    return user