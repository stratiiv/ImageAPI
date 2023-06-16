from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ImageSerializer
from .models import Image
from .permissions import IsAuthorOrReadOnly


class ImageViewSet(ModelViewSet):
    """Provides CRUD endpoints on Image"""
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Auto add author as a current user when creating"""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Auto add author as a current user when updating"""
        serializer.save(author=self.request.user)