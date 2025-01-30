from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from foodie_api.permissions import IsOwnerOrReadOnly
from posts.models import Post, Tag
from posts.serializers import TagSerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PostPagination(PageNumberPagination):
  page_size = 10
  page_size_query_param = "page_size"
  max_page_size = 100

class PostListCreateView(generics.ListCreateAPIView):
  """
  List all posts or create a post if logged in.
  """
  
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  queryset = Post.objects.annotate(
    likes_count=Count('likes', distinct=True),
    comments_count=Count('comments',distinct=True)
  ).order_by('-created_at')
  
  pagination_class = PostPagination
  filter_backends = [
    filters.OrderingFilter,
    filters.SearchFilter,
    DjangoFilterBackend,
    ]
  filterset_fields = [
    'author__profile',
    'category',
    'tags',
    'likes__author__profile',
    'author__followed__author__profile',
    ]
  search_fields = [
    'title',
    'content',
    'tags__name',
    'category',
    'author__username',
    ]
  ordering_fields = [
    'likes_count',
    'comments_count',
    'likes__created_at',
    ]
  
  def perform_create(self, serializer):
    """
    Assign the logged-in user as the author when creating a post
    """
    serializer.save(author=self.request.user)
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
  """
  Retrive a post and edit or delete it if the user is the author
  """
  
  serializer_class = PostSerializer
  permission_classes = [IsOwnerOrReadOnly]
  queryset = Post.objects.annotate(
    likes_count=Count('likes', distinct=True),
    comments_count=Count('comments',distinct=True)
  ).order_by('-created_at')
  
class TagListCreateView(generics.ListCreateAPIView):
  """
  List all tags or create a tag.
  """
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['name']