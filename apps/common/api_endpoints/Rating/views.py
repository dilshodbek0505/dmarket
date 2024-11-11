from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.common.models import Rating
from .serializers import RatingSerializer

class RatingCreateApi(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

__all__ = [
    'RatingCreateApi',
]