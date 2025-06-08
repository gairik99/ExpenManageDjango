from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Allow access if the user is the author of the object
        return obj.user_name == request.user