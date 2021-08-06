from rest_framework import permissions


class IsUsersProfile(permissions.BasePermission):
    """
    Custom permission to only allow users to view their own profile info.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
