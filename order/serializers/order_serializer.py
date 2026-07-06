from rest_framework import serializers
from order.models import Order
from product.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["product", "total"]

    def get_total(self, instance):
        return sum(p.price for p in instance.product.all())