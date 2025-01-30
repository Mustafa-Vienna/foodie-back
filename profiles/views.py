from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from foodie_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfilePagination(PageNumberPagination):
  page_size = 10
  page_size_query_param = "page_size"
  max_page_size = 100


class ProfileList(generics.ListAPIView):
  """
  List all profiles.
  """
  queryset = Profile.objects.annotate(
    posts_count=Count('author__posts', distinct=True),
    followers_count=Count('author__followed', distinct=True),
    following_count=Count('author__following', distinct=True)
  ).order_by('-created_at')
  serializer_class = ProfileSerializer
  pagination_class = ProfilePagination
  filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
  filterset_fields = [
    'author__following__followed__profile',
    'author__followed__author__profile'
  ]
  ordering_fields = [
    'posts_count',
    'followers_count', 
    'following_count', 
    'author__following__created_at',
    'author__followed__created_at',
    ]
  
  
class ProfileDetail(generics.RetrieveUpdateAPIView):
  """
  Retrive or update a profile if you're the owner
  """
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Profile.objects.annotate(
    posts_count=Count('author__posts', distinct=True),
    followers_count=Count('author__followed', distinct=True),
    following_count=Count('author__following', distinct=True)
  ).order_by('-created_at')
  serializer_class = ProfileSerializer
      
    
