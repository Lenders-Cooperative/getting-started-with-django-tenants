from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel


class Author(TimeStampedModel, UUIDModel):
    name = models.CharField(_("Author name"), max_length=50)
    email = models.EmailField(_("Author email"), max_length=254)
    gender = models.CharField(_("Author Gender"), max_length=10)
    date_of_birth = models.DateField(_("Author Date of Birth"), auto_now=False, auto_now_add=False)


class Article(TimeStampedModel, UUIDModel):
    author = models.ForeignKey("knowledge_base.Author", verbose_name=_("Authored by"), on_delete=models.CASCADE)
    title = models.TextField(_("Title"))
    entry = models.TextField(_("Article Entry"))
