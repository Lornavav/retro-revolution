from django.contrib import admin
from .models import Collectable, Platform, Genre


class CollectableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'platform',
        'genre',
        'year',
        'price'
    )

    ordering = ('name',)

class PlatformAdmin(admin.ModelAdmin):
    ordering = ('name',)


class GenreAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Collectable, CollectableAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
