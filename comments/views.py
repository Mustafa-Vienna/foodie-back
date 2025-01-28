from rest_framework import generics, permissions
from foodie_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
  serializer_class = CommentSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Comment.objects.all()
  
  def perform_create(self, serializer):
    post_id = self.request.data.get('post')
    serializer.save(author=self.request.user, post_id=post_id)
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentDetailSerializer
  permission_classes = [IsOwnerOrReadOnly]