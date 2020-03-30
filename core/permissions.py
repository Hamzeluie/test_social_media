from rest_framework.permissions import BasePermission
from rest_framework import permissions


class UpdateOwnPosts(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.id == request.user.id


class UpdateOwnComments(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.post.author.id == request.user.id


class UpdateOwnProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id