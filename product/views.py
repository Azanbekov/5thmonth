from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Product, Category, Review
from .serializers import (
    ProductSerializer, ProductsSerializer,
    CategoriesSerializer, ReviewSerializer,
    ReviewsSerializer, ProductsReviewSerializer
)

class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductSerializer
        return ProductsSerializer


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'id'

class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReviewSerializer
        return ReviewsSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class ProductReviewListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsReviewSerializer


