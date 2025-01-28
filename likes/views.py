from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer


class LikeListCreateView(generics.ListCreateAPIView):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    
class LikeDetailView(generics.RetrieveDestroyAPIView):
  queryset = Like.objects.all()
  serializer_class = LikeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]