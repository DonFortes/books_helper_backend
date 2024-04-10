from books.models import Book
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "author", "price"]
    search_fields = ["name", "title", "author", "price"]
    list_filter = ["name", "title", "author", "price"]
