from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_finished', 'rating')
    list_filter = ('author', 'rating', 'date_finished')
    search_fields = ('title', 'author')
    ordering = ('title',)