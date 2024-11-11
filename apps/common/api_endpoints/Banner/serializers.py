from rest_framework import serializers
from apps.common.models import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('title', 'image', 'phone_image', 'order')
