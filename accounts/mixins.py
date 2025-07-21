from django.http import HttpResponseForbidden

class RoleRequiredMixin:
    required_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_authenticated and hasattr(request.user, 'profile')):
            return HttpResponseForbidden("You must be logged in.")
        if request.user.profile.role not in self.required_roles:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)
