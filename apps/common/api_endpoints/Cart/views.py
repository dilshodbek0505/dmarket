from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.common.models import Cart, CartItem
from apps.common.api_endpoints.Cart.serializers import CartSerializer, CartItemSerializer


class CartDetailApi(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class CartItemCreateApi(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class CartItemDeleteApi(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return self.queryset.filter(cart=cart)

__all__ = [
    'CartDetailApi',
    'CartItemCreateApi',
    'CartItemDeleteApi',

]