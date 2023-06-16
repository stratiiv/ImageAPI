from rest_framework.viewsets import ModelViewSet
from .serializers import ImageSerializer
from .models import Image


class ImageViewSet(ModelViewSet):
    """Provides CRUD endpoints on Image"""
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def perform_create(self, serializer):
        """Auto add author as a current user when creating"""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Auto add author as a current user when updating"""
        serializer.save(author=self.request.user)