from rest_framework import serializers
from apps.common.models import Order, OrderItem, ProductSize


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductSize.objects.all())

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'total_price')
        read_only_fields = ('total_price',)


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'delivery_time', 'is_discount', 'address', 'order_items', 'total_price')
        read_only_fields = ('user', 'total_price')
