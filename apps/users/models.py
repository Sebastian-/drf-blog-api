from django.contrib.auth.models import AbstractUser

# Docs recommend creating a custom user at the start of any project
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project


class User(AbstractUser):
    pass
