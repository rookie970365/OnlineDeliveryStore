from django.contrib import admin
from blog.models import Post, Author, Tag
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "pk", "title", "author", "created"
    list_display_links = "pk", "title"
    ordering = "-created", "pk"
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"
