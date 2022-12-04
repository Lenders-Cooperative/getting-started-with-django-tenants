from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, unique=True)
    details = models.CharField(max_length=100)


class OrganizationModel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        abstract = True
