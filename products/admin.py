from django.contrib import admin
from .models import Collectable, Platform, Genre

admin.site.register(Collectable)
admin.site.register(Platform)
admin.site.register(Genre)
