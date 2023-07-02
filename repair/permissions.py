from rest_framework import permissions

ALLOWED_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')


class ServicemanPermissions(permissions.BasePermission):
    """
    Определяет правила простомтра и редактирования списка ремонтников
    Только главный мастер может добавлять и удалять ремонтников
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user:
            return True

        return bool(request.user)

    def has_object_permission(self, request, view, obj):
        return bool(request.user)


class OrderPermissions(permissions.BasePermission):
    """
    Определяет правила простомтра и редактирования списка закзов
    """

    def has_permission(self, request, view):
        if request.method in ALLOWED_METHODS and request.user:
            return True

        return bool(request.user)

    def has_object_permission(self, request, view, obj):
        return bool(request.user)
