from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.categories.models import Category  

User = get_user_model()

class CategoryTests(APITestCase):
    """Testes para criação e listagem de categorias"""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword123")
        self.token = str(RefreshToken.for_user(self.user).access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.category = Category.objects.create(name="Automotivos")

        self.create_category_url = "/api/categories/"
        self.list_categories_url = "/api/categories/"

    def test_create_category_authenticated(self):
        response = self.client.post(self.create_category_url, {"name": "Eletrônicos"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_list_categories_authenticated(self):
        response = self.client.get(self.list_categories_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
