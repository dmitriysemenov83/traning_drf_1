from django.urls import path
from products.apps import ProductsConfig
from products.views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='products_list'),
    path('retrive/<int:pk>/', ProductRetrieveAPIView.as_view(), name='products_retrive'),
    path('create/', ProductCreateAPIView.as_view(), name='products_create'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='products_update'),
    path('delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='products_delete'),
]
