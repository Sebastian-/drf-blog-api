from django.db.models import fields
from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    viewcount = serializers.ReadOnlyField(source='viewcount.count')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    class Meta:
        model = Post
        fields = ['id', 'title', 'time_created',
                  'time_edited', 'author', 'viewcount', 'body']
        extra_kwargs = {'body': {'write_only': True}}


class PostDetailSerializer(PostListSerializer):

    class Meta(PostListSerializer.Meta):
        extra_kwargs = {}
