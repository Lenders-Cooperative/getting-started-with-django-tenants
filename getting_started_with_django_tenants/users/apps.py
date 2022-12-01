from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "getting_started_with_django_tenants.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import getting_started_with_django_tenants.users.signals  # noqa F401
        except ImportError:
            pass
