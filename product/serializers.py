from rest_framework import serializers
from .models import Product, Category, Review
from django.db.models import Avg


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars'.split()

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class ProductsReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description','reviews', 'average_rating']

    def get_average_rating(self, obj):
        result = obj.reviews.aggregate(avg=Avg('stars'))
        return round(result['avg'], 1) if result['avg'] else 0


class CategoriesSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()
