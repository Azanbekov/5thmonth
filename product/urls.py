from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),  # ✅ Исправлено
    path('products/<int:id>/', views.ProductDetailAPIView.as_view()),  # если есть детальный просмотр
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('reviews/', views.ReviewListAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('products/reviews/', views.ProductReviewListAPIView.as_view()),
]
