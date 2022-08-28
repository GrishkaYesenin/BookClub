from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'writer', 'datetime')
    list_display_links = ('name',)
    search_fields = ('name', 'writer', 'datetime')


admin.site.register(Book, BookAdmin)