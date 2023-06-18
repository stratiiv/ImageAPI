from io import BytesIO

import pytest
from PIL import Image as PILimage
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from rest_framework.test import APIClient
from rest_framework import status

from .models import Image


@pytest.fixture
def user():
    return User.objects.create(username='testuser', password='testpass')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def image_file(request):
    image = PILimage.new('RGB', (800, 600))
    image_buffer = BytesIO()
    image.save(image_buffer, format='JPEG')
    uploaded_file = SimpleUploadedFile('test_image.jpg',
                                       image_buffer.getvalue(),
                                       content_type='image/jpeg')
    return uploaded_file


@pytest.mark.django_db
def test_create_image(api_client, user, image_file):
    api_client.force_authenticate(user=user)

    data = {
        'name': 'Test image',
        'image': image_file,
    }
    url = reverse('image-list')
    response = api_client.post(url, data, format="multipart")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Test image'
    assert 'image' in response.data
    assert 'preview' in response.data
    assert 'type' in response.data
    assert 'author' in response.data
    assert response.data['author'] == user.id

    image_id = response.data['id']
    image = Image.objects.get(id=image_id)

    # Check if preview image is generated and saved correctly
    preview_path = image.preview.path
    assert default_storage.exists(preview_path) 

    # Validate the preview image size
    with PILimage.open(preview_path) as preview_image:
        width, height = preview_image.size
        assert width <= 100
        assert height <= 100


@pytest.mark.django_db
def test_update_image(api_client, user, image_file):
    api_client.force_authenticate(user=user)

    data = {
        'name': 'Test Image',
        'image': image_file,
    }

    url = reverse('image-list')
    response = api_client.post(url, data, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
    image_id = response.data['id']

    url = reverse('image-detail', kwargs={'pk': image_id})
    updated_data = {
        'name': 'Updated Image',
    }
    response = api_client.patch(url, updated_data)

    assert response.status_code == status.HTTP_200_OK, response.data
    assert response.data['name'] == 'Updated Image'
    assert 'image' in response.data
    assert 'preview' in response.data
    assert 'type' in response.data
    assert 'author' in response.data
    assert response.data['author'] == user.id


@pytest.mark.django_db
def test_delete_image(api_client, user, image_file):
    api_client.force_authenticate(user=user)

    data = {
        'name': 'Test Image',
        'image': image_file,
    }

    url = reverse('image-list')
    response = api_client.post(url, data, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
    image_id = response.data['id']

    url = reverse('image-detail', kwargs={'pk': image_id})
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT

    url = reverse('image-detail', kwargs={'pk': image_id})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_upload_large_file(api_client, user):
    api_client.force_authenticate(user=user)

    # Create a large file with a size greater than 10MB
    large_file = SimpleUploadedFile("large_image.jpg",
                                    b"X" * (11 * 1024 * 1024),
                                    content_type="image/jpeg")

    data = {
        'name': 'Large Image',
        'image': large_file,
    }
    url = reverse('image-list')
    response = api_client.post(url, data, format="multipart")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Image.objects.count() == 0