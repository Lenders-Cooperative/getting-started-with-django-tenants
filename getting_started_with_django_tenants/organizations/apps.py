from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrganizationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "getting_started_with_django_tenants.organizations"
    verbose_name = _("Organizations")
