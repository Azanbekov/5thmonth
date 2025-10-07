from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import ProductSerializer, ProductsSerializer, CategoriesSerializer, ReviewSerializer, ReviewsSerializer, ProductsReviewSerializer
from django.db.models import Avg


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductsSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product, many=False).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategoriesSerializer(categories, many=True).data


    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    data = CategoriesSerializer(category, many=False).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewsSerializer(reviews, many=True).data


    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)


@api_view(['GET'])
def product_review_list_api_view(request):
    products = Product.objects.all()
    data = ProductsReviewSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategoriesSerializer(categories, many=True).data
    return Response(data=data, status=200)
