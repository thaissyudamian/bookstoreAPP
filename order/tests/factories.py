import factory
from django.contrib.auth.models import User
from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "senha123")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.product.add(product)