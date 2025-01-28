# permissions.py
from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow only owners (trainers) or admins to edit or delete the course.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is the trainer (owner) of the course or an admin
        return request.user == obj.trainer or request.user.is_staff
