from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'teacherprofile')
