from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    viewcount = serializers.ReadOnlyField(source='viewcount.count')

    class Meta:
        model = Post
        fields = ['id', 'title', 'time_created',
                  'time_edited', 'author', 'viewcount']
