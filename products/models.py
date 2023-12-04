from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    stock_amount = models.IntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(1)])
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def product_in_stock(self):
        if self.stock_amount >= 1:
            return True
        else:
            return False
    
    def save(self, *args, **kwargs):
        self.in_stock = self.product_in_stock()
        super().save(*args, **kwargs)

class SellCollectable(models.Model):
    collectable_item = models.CharField(max_length=250, null=False, blank=False)
    platform = models.ForeignKey(
        'Platform', null=True, blank=True, on_delete=models.SET_NULL)
    additional_information = models.TextField(null=True, blank=True)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    contact_number = models.CharField(max_length=250, null=False, blank=False)
    email = models.CharField(max_length=250, null=False, blank=False)
    image = CloudinaryField('image')

    def __str__(self):
        return self.collectable_item
    

class Review(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    product_type = models.ForeignKey(
        'Platform', null=True, blank=True, on_delete=models.SET_NULL)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.full_name}"
