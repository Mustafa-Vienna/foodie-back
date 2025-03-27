from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from foodie_api.permissions import IsOwnerOrReadOnly


class FollowerListCreateView(generics.ListCreateAPIView):
    queryset = Follower.objects.select_related('author', 'followed').all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
