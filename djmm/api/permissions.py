from rest_framework.permissions import BasePermission
from .models import Backtest

class IsOwner(BasePermission):
    """Class permission to allow only backtest owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the backtest owner."""
        if isinstance(obj, Backtest):
            """2DO+++ This is probably where we change the name to obj.server instead"""
            return obj.owner == request.user
        return obj.owner == request.user
