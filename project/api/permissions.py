from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the message
        return obj.owner == request.user


class IsUser(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own user object
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the message
        return obj == request.user


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the message
        return obj.owner == request.user


class IsUserIncluded(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user in set(obj.users.all())
