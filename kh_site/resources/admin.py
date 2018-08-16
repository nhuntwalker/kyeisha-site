from django.contrib import admin
from resources.models import Book, Resource, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Administrator for the Book object."""

    fields = ['title', 'author', 'categories', 'cover_image', 'link', 'position']
    list_display = ['title', 'author', 'position']
    list_filter = ['categories']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """Administrator for the Resource object."""

    list_display = ['title', 'phone_number', 'position']


admin.site.register(Category)
