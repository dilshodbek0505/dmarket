from rest_framework import serializers

from apps.common.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("product", "rating")
        