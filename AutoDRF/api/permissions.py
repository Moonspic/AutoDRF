from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class ClassName_Permission(BasePermission): 
    def has_permission(self, request, view):
        return True 

    def has_object_permission(self, request, view, obj):
        #if obj.creator == request.user:
            #return True 
        return True 

