from django.db.models import Count
from rest_framework import generics, permissions, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from foodie_api.permissions import IsOwnerOrReadOnly
from posts.models import Post, Tag
from posts.serializers import TagSerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PostListCreateView(generics.ListCreateAPIView):
    """
    List all posts or create a post if logged in.
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
      likes_count=Count('likes', distinct=True),
      comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')

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
        comments_count=Count('comments', distinct=True)
        ).order_by('-created_at')


class PostEditView(generics.UpdateAPIView):
    """
    Edit a post if the user is the author
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
             instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class TagListCreateView(generics.ListCreateAPIView):
    """
    List all tags or create a tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
