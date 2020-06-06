from django.contrib import admin
from .models import *


admin.site.register(Comment)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'rating', 'release')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}