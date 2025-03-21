from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from foodie_api.permissions import IsOwnerOrReadOnly


class LikeListCreateView(generics.ListCreateAPIView):
  queryset = Like.objects.select_related('author', 'post').all()
  serializer_class = LikeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    
class LikeDetailView(generics.RetrieveDestroyAPIView):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
  permission_classes = [IsOwnerOrReadOnly]