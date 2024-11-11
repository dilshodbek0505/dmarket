from rest_framework import serializers

from apps.common.models import Product, ProductSize
from apps.common.api_endpoints.Category.serializers import CategorySerializer



class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ('id', 'name', 'size', 'price', 'description', 'image')



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    product_sizes = ProductSizeSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'rating', 'image', 'product_sizes')


class ProductSerializerShort(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'rating', 'image')