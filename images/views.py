from rest_framework.viewsets import ModelViewSet
from .serializers import ImageSerializer
from .models import Image


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    