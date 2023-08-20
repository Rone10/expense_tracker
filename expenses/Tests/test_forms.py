import pytest
from expenses.forms import ExpenseForm

pytestmark = pytest.mark.django_db


class TestExpenseForm:
    def test_form(self):
        form = ExpenseForm(data={})
        assert form.is_valid() is False, "Should be invalid if no data is given"

        form = ExpenseForm(data={"amount": 100, "name": "test form name", "category": "Personal"})
        assert form.is_valid() is True, "Should be valid if all required fields are given"

