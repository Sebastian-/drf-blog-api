import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Post(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=300)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),
                               related_name='posts',
                               on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Update time_edited whenever the post is edited
        """
        if self.id:
            # only update if post already exists
            self.time_edited = timezone.now()

        super(Post, self).save(*args, **kwargs)

    def increment_view_count(self):
        self.viewcount.count += 1
        self.viewcount.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time_created']


class ViewCount(models.Model):
    count = models.PositiveIntegerField('view count', default=0)
    post = models.OneToOneField(Post,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return f'{str(self.count)} views for {self.post.title}'
