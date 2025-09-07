from django.contrib import admin

from .models import Category, Note


class CategoryAdmin(admin.ModelAdmin):
    ...


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'user']


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
