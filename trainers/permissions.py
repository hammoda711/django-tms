from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsTrainerOwner(BasePermission):
    """
    Custom permission to allow access only if the logged-in user is a trainer and is updating their own profile.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Ensure the logged-in user is a trainer and matches the trainer ID in the URL
        return obj.user.id == request.user.id


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission to allow access to the trainer's profile if the user is the owner or an admin.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # If the user is admin, they can access any trainer profile
        if request.user.is_staff:
            return True
        
        # If the user is the owner of the trainer profile, they can access their own
        if obj.user.id == request.user.id:
            return True
        
        # If neither condition is met, permission is denied
        raise PermissionDenied("You do not have permission to access this trainer's profile.")

class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
