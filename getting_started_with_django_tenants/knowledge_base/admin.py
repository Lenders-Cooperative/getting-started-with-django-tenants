from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from .models import Article, Author


class AuthorAdmin(admin.ModelAdmin, DjangoQLSearchMixin):
    model = Author
    list_display = ("id", "name", "email")


class ArticleAdmin(admin.ModelAdmin, DjangoQLSearchMixin):
    list_display = ("id", "author", "title")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
