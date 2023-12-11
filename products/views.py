from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
