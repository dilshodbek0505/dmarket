from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ProductSerializer, ProductSerializerShort
from apps.common.models import Product


class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class ProductListShortApi(ListAPIView):
    serializer_class = ProductSerializerShort
    queryset = Product.objects.all()

class ProductRetrieveApi(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


__all__ = [
    'ProductListApi',
    'ProductListShortApi',
    'ProductRetrieveApi',
]