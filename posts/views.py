from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from foodie_api.permissions import IsOwnerOrReadOnly
from posts.models import Post, Tag
from posts.serializers import TagSerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostListCreateView(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['category', 'tags']
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsOwnerOrReadOnly]
  
class TagListCreateView(generics.ListCreateAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer