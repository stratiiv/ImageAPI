from django.db import models
from .services import (generate_preview_image, get_image_extension,
                       validate_image)


class Image(models.Model):
    """Represents image entity."""
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', validators=[validate_image])
    preview = models.ImageField(upload_to='images/previews', blank=True,
                                null=True)   
    type = models.CharField(max_length=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        """Generate type and preview of image before saving."""
        self.type = get_image_extension(self.image.name)
        image_data = self.image.read()  # Read the image data
        preview_path = generate_preview_image(image_data, self.image.name)
        self.preview = preview_path
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.image.name}"
