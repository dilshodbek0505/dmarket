from rest_framework.generics import ListAPIView

from apps.common.models  import Category
from .serializers import CategorySerializer


class CategoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


__all__ = ['CategoryListApi']