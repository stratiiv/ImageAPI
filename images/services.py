import sys
import os
from PIL import Image
from django.conf import settings


PREVIEW_SIZE = (100, 100)

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def generate_preview_image(image_path: str, preview_filename: str) -> None:
    """Generate a preview image from the original image.

    This function opens the original image, resizes it to the specified
    preview size, and saves it as a PNG file in the previews directory.
    """
    with Image.open(image_path) as im:
        print(preview_filename)
        im.convert("RGB")
        im.thumbnail(PREVIEW_SIZE)
        preview_path = os.path.join(settings.MEDIA_ROOT, 'images', 'previews',
                                    preview_filename.replace("webp", "png"))
        im.save(preview_path, "png")
