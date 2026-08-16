from rest_framework.permissions import BasePermission
from .models import UserProfile


class IsPremiumUser(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        try:
            profile = UserProfile.objects.get(
                user=request.user
            )

            return profile.is_premium

        except UserProfile.DoesNotExist:
            return False