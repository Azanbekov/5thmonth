from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True) 

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        result = self.reviews.aggregate(avg=Avg('stars'))
        return round(result['avg'], 1) if result['avg'] else 0


STARS = ((i, '* ' * i) for i in range(1, 6))


class Review(models.Model):
    text = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=1, null=True, blank=True)

    def __str__(self):
        return self.text
    

