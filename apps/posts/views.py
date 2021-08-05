from rest_framework import generics, permissions

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
