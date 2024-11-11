from django.urls import path

from apps.common.api_endpoints import *
from apps.common.views import health_check_redis

app_name = "common"

urlpatterns = [
    path("VersionHistory/", VersionHistoryView.as_view(), name="version-history"),
    path("CategoryList/", CategoryListApi.as_view(), name='category-list'),
    path("ProductList/", ProductListApi.as_view(), name='product-list'),
    path("ProductListShort/", ProductListShortApi.as_view(), name='product-list-short'),
    path("ProductDetail/<uuid:pk>/", ProductRetrieveApi.as_view(), name='product-retrieve'),
    path("RatingCreate/", RatingCreateApi.as_view(), name='rating-create'),
    path("CartDetail/<uuid:pk>/", CartDetailApi.as_view(), name='cart-detail'),
    path("CartItemCreate/", CartItemCreateApi.as_view(), name='cart-create'),
    path("CartItemDelete/<uuid:pk>/", CartItemDeleteApi.as_view(), name='cart-delete'),
    path("OrderDetail/<uuid:pk>/", OrderDetailApi.as_view(), name='order-detail'),
    path("OrderItemCreateApi/", OrderItemCreateApi.as_view(), name='order-item-create'),
    path("BannerList/", BannerListApi.as_view(), name='banner-list'),
    path("health-check/redis/", health_check_redis, name="health-check-redis"),
]
