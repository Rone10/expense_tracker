from .factories import ExpenseFactory
from expenses.models import Expense
import pytest


pytestmark = pytest.mark.django_db


class TestExpenseModel:
    def test_expense_model(self):
        expense = ExpenseFactory(
            name="Test Expense",
        )
        assert isinstance(expense, Expense)
        assert expense.__str__() == expense.name
        assert str(expense) == 'Test Expense'

