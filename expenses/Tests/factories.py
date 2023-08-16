import factory
from expenses.models import Expense


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    name = factory.Faker('word')
    amount = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    date = factory.Faker('date')
    category = factory.Faker('word')