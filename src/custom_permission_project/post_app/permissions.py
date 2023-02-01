from rest_framework import permissions

class IsOwnerOrReadOnlyOrCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(True)
        return bool(request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(True)
        return bool(request.user and request.user.is_authenticated and (request.user.role == "ADMIN" or request.user == obj.created_by))