from django.urls import path

from getting_started_with_django_tenants.organizations.views import current_datetime

app_name = "organizations"
urlpatterns = [
    path("", view=current_datetime, name="index"),
]
