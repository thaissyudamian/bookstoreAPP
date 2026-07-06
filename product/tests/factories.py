import factory

from django.contrib.auth.models import User
from product.models import Category, Product
from order.models import Order

class CategoryFactory(factory.django.DjangoModelFactory):
    title = "..."
    slug = "..."
    description = "..."
    active = True
    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    title = "..."
    price = 10.0
    class Meta:
        model = Product
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if extracted:
            for cat in extracted:
                self.category.add(cat)

class UserFactory(factory.django.DjangoModelFactory):
    email = "user@example.com"
    username = "user"
    class Meta:
        model = User          # model pronto do Django (reaproveitado)

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    class Meta:
        model = Order
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if extracted:
            for prod in extracted:
                self.product.add(prod)