from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)  

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ["user"]
