from django.contrib import admin
from isbnlib import meta, cover

# Register your models here.

from .models import book

#admin.site.register(book)
@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display = ('ISBN', 'price', 'count')
    list_editable = ('count',)

