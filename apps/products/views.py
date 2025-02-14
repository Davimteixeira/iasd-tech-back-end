from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    """Permite listar e criar produtos apenas para o usuário autenticado"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Lista apenas os produtos do usuário autenticado"""
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Define o usuário autenticado como o dono do produto"""
        serializer.save(user=self.request.user)
