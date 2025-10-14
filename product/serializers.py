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

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название категории не может быть пустым.")
        if Category.objects.filter(name__iexact=value.strip()).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название продукта не может быть пустым.")
        if len(value) < 2:
            raise serializers.ValidationError("Название продукта должно быть длиннее 2 символов.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше 0.")
        return value

    def validate(self, attrs):
        if attrs.get('description') and len(attrs['description']) < 10:
            raise serializers.ValidationError("Описание должно содержать не менее 10 символов.")
        return attrs

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'product']

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст отзыва не может быть пустым.")
        if len(value) < 3:
            raise serializers.ValidationError("Отзыв должен быть длиной не менее 3 символов.")
        return value