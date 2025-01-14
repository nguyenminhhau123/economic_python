
from django.urls import path
from base.views import product_views as views


urlpatterns = [
  
    path('',views.getProducts, name='products'),
    path('create/',views.createProduct, name='product-create'),
    path('<str:pk>/',views.getProduct, name='product'),
    path('delete/<str:pk>/',views.deleteProduct, name='product-delete'),
    path('update/<str:pk>/',views.updateProduct, name='product-update'),
    path('img/upload/',views.uploadImage, name='image-upload'),
    path('rating/top/',views.getTopProducts, name='top-product'),
]