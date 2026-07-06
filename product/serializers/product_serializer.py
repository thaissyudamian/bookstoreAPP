from rest_framework import serializers
from product.models import Product
from .category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "active", "category"]