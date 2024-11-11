from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.common.models import Banner
from apps.common.api_endpoints.Banner.serializers import BannerSerializer


class BannerListApi(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


__all__ = [
    'BannerListApi',
]