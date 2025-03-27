from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from foodie_api.permissions import IsOwnerOrReadOnly


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.select_related('author', 'post').all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get("post")

        if post_id:
            queryset = queryset.filter(
                post_id=post_id, author=self.request.user
                 )
        elif self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LikeDeleteByPostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        user = self.request.user
        try:
            like = Like.objects.get(post_id=post_id, author=user)
            self.check_object_permissions(self.request, like)
            return like
        except Like.DoesNotExist:
            raise NotFound("You have not liked this post.")

    def delete(self, request, *args, **kwargs):
        like = self.get_object()
        like.delete()
        return Response(status=204)
