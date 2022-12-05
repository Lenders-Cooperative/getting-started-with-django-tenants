from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Domain, Organization


@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name", "tenant_type", "is_enabled", "in_production")


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("domain", "created", "modified")
