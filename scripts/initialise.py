from django.conf import settings
from django.contrib.auth import get_user_model
from django_tenants.utils import get_tenant_model

User = get_user_model()


def create_superuser():
    global_superuser = User.objects.create_superuser(
        name="Jatin Goel",
        username="jatin",
        email="jatin.goel@thesummitgrp.com",
        password="qwerty123",
        is_superuser=True,
        is_staff=True,
    )

    print("Created user: ", global_superuser)


def create_public_tenant():
    tenant = get_tenant_model()(
        tenant_type=settings.PUBLIC_TENANT_NAME,
        schema_name=settings.PUBLIC_TENANT_NAME,
        name="Jatin Goel's public tenant.",
        is_enabled=True,
        in_production=False,
    )
    tenant.save()

    # get_tenant_domain_model().objects.get_or_create(
    #     domain=get_tenant_domain_model().standard_domain_from_schema_name(schema.schema_name),
    #     tenant=schema,
    #     is_primary=True,
    # )

    # # Add one or more domains for the tenant
    # domain = Domain()
    # domain.domain = (
    #     "localtest.me"  # don't add your port or www here! on a local server you'll want to use localhost here
    # )
    # domain.tenant = tenant
    # domain.is_primary = True
    # domain.save()


def run(*args):
    create_superuser()
    create_public_tenant()
