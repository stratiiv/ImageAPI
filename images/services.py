import sys
import os
from PIL import Image
from django.conf import settings
from django.core.exceptions import ValidationError

PREVIEW_SIZE = (100, 100)

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def generate_preview_image(image_path: str, image_name: str) -> str:
    """Generate a preview image from the original image.

    This function opens the original image, resizes it to the specified
    preview size, and saves it as a PNG file in the previews directory.
    """
    preview_filename = f"preview_{os.path.basename(image_name)}"
    preview_filename = os.path.splitext(preview_filename)[0] + ".png"
    with Image.open(image_path) as im:
        im.convert("RGB")
        im.thumbnail(PREVIEW_SIZE)
        preview_path = os.path.join(settings.MEDIA_ROOT, 'images', 'previews',
                                    preview_filename)
        im.save(preview_path, "png")
    return os.path.join('images', 'previews', preview_filename).replace("\\", "/")


def get_image_extension(image_name: str) -> str:
    return os.path.splitext(image_name)[1].lstrip('.')
