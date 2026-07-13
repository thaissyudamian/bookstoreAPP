import pytest
from order.serializers import OrderSerializer
from order.tests.factories import OrderFactory
from product.tests.factories import ProductFactory


@pytest.mark.django_db
def test_order_serializer_total():
    product1 = ProductFactory(price=50)
    product2 = ProductFactory(price=30)
    order = OrderFactory(product=[product1, product2])

    serializer = OrderSerializer(instance=order)
    data = serializer.data

    assert data["total"] == 80
    assert len(data["product"]) == 2