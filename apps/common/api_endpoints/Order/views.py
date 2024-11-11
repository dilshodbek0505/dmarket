from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.common.models import Order, OrderItem
from apps.common.api_endpoints.Order.serializers import OrderSerializer, OrderItemSerializer


class OrderDetailApi(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order, _ = Order.objects.get_or_create(user=self.request.user)
        return order


class OrderItemCreateApi(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order, _ = Order.objects.get_or_create(user=self.request.user)
        serializer.save(order=order)

__all__ = [
    'OrderDetailApi',
    'OrderItemCreateApi',
]