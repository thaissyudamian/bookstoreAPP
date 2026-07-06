import pytest
from product.serializers import ProductSerializer
from product.tests.factories import CategoryFactory, ProductFactory

@pytest.mark.django_db
def test_category_factory_cria_categoria():
    category = CategoryFactory(title="Livros")
    assert category.id is not None
    assert category.title == "Livros"

@pytest.mark.django_db
def test_product_serializer_retorna_campos():
    category = CategoryFactory(title="Livros")
    product = ProductFactory(title="Django REST", price=99.90, category=[category])
    serializer = ProductSerializer(instance=product)
    data = serializer.data
    assert data["title"] == "Django REST"
    assert len(data["category"]) == 1
    assert data["category"][0]["title"] == "Livros"