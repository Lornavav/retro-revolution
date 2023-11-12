from django.db import models
from cloudinary.models import CloudinaryField


class Platform(models.Model):
    name = models.CharField(max_length=254)
  
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Collectable(models.Model):
    platform = models.ForeignKey(
        'Platform', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254)
    description = models.TextField()
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
