from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.products.models import Product 
from apps.categories.models import Category

User = get_user_model()

class ProductTests(APITestCase):
    """Testes para criação e listagem de produtos"""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpassword123")
        self.category = Category.objects.create(name="Eletrônicos")

        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.product_data = {
            "name": "Smartphone",
            "description": "Novo modelo com câmera de alta resolução",
            "price": "1999.99",
            "category": self.category.id
        }

        self.create_product_url = "/api/products/"
        self.list_products_url = "/api/products/"

    def test_create_product_authenticated(self):
        response = self.client.post(self.create_product_url, self.product_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_list_products_authenticated(self):
        Product.objects.create(user=self.user, category=self.category, **self.product_data)
        response = self.client.get(self.list_products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
