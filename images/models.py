import os
from django.db import models
from .services import generate_preview_image


class Image(models.Model):
    """Represents image entity."""
    name = models.CharField(max_length=255)
    image_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    preview = models.CharField(max_length=255, blank=True, null=True)  # URL for preview

    def save(self, *args, **kwargs):
        """Generate and save the preview image."""
        super().save(*args, **kwargs)
        preview_path = generate_preview_image(self.image.path, self.image.name)
        self.preview = preview_path
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.image.name}"
