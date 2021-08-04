from django import dispatch
from django.apps import AppConfig
from django.db.models import signals


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.posts'

    def ready(self):
        # attach signal handlers
        from .models import Post
        from .signals import create_post_viewcount

        signals.post_save.connect(create_post_viewcount,
                                  sender=Post,
                                  weak=False,
                                  dispatch_uid='post_save_create_post_viewcount')

        return super().ready()
