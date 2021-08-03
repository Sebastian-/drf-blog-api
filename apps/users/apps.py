from django.apps import AppConfig

# nested apps require updated name
# https://stackoverflow.com/questions/67056517/django-3-2-exception-django-core-exceptions-improperlyconfigured


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
