# ImageAPI

ImageAPI is a RESTful API for managing and serving images. It provides CRUD endpoints for image entities, including features like image upload, preview generation, and authorization controls.

## Technologies Used

- Python
- Django
- Django REST Framework

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install `pipenv` if you haven't already:
```bash
pip install pipenv
```
4. Install the project dependencies using pipenv:
```bash
pipenv install
```
5. Create a .env file in the project root directory. Add the following line to the file, replacing your_secret_key_here with your actual secret key:
```
DJANGO_SECRET_KEY=your_secret_key_here
```
6. Launch the virtual environment:
```bash
pipenv shell
```

7. Apply database migrations:

```bash
python manage.py migrate
```
8. Run the application using:
```bash
python manage.py runserver
```
The API will be accessible at `http://localhost:8000/`.

## API Endpoints
The API provides the following endpoints:

* `GET /images/`: Retrieve a list of all images.
* `POST /images/`: Upload a new image.
* `GET /images/{id}/`: Retrieve details of a specific image.
* `PUT /images/{id}/`: Update an existing image.
* `DELETE /images/{id}/`: Delete an existing image.
For detailed information about each endpoint and the required/request/response formats, please refer to the API documentation.

## Authentication and Permissions
The API uses token-based authentication. To access authenticated endpoints, include an Authorization header in your requests with the value Token {your_token}. Tokens can be obtained by logging in or creating a new user account.

The API enforces permissions based on the user's role. By default, users can create, read, update, and delete their own images. Administrators have full access to all images.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

ImageAPI is open source and released under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details.

