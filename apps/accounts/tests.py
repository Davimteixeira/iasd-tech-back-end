from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class AuthTests(APITestCase):

    def setUp(self):
        """Configuração inicial para os testes de autenticação"""
        self.register_url = "/api/register/"
        self.login_url = "/api/login/"
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_register_user(self):
        """Teste para registrar um usuário"""
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)

    def test_login_user(self):
        """Teste para login do usuário e obtenção de token"""
        response = self.client.post(self.login_url, {
            "email": self.user_data["email"],
            "password": self.user_data["password"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_login_fails_with_wrong_password(self):
        """Teste de falha no login com senha errada"""
        response = self.client.post(self.login_url, {
            "email": self.user_data["email"],
            "password": "wrongpassword"
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
