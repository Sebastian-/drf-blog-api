from .models import ViewCount


def create_post_viewcount(sender, instance, created, **kwargs):
    """
    Create and associate a view count whenever a new post is made
    """
    if created:
        ViewCount.objects.create(post=instance)
