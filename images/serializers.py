from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image', 'preview', 'type', 'author')
        read_only_fields = ('preview', 'type', 'author')