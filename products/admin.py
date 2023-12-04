from django.contrib import admin
from .models import Collectable, Platform, Genre, SellCollectable, Review


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

class SellCollectableAdmin(admin.ModelAdmin):
    list_display = (
        'collectable_item',
        'platform',
        'additional_information',
        'full_name',
        'contact_number',
        'email',
        'image'
    )

class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'product_type',
        'body',
        'created_on',
    )

    ordering = ('created_on',)

admin.site.register(Review, ReviewsAdmin)
admin.site.register(Collectable, CollectableAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(SellCollectable, SellCollectableAdmin)
