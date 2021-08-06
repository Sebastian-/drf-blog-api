from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # this call is explicitly required to ensure create_user receives the correct arguments
        # https://stackoverflow.com/questions/44440652/django-cant-login-after-creating-user
        user = get_user_model().objects.create_user(**validated_data)
        return user

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
