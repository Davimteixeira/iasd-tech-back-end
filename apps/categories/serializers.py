from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    """Serializer para listar e criar categorias"""

    class Meta:
        model = Category
        fields = "__all__"
