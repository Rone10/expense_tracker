from django.urls import reverse
import pytest
from expenses.models import Expense
from expenses.forms import ExpenseForm
from expenses.views import (
            ExpenseListView, ExpenseDetailView,
            ExpenseCreateView, ExpenseUpdateView, ExpenseUpdateView,
            ExpenseDeleteView, 

        ) 
from expenses.tests.factories import ExpenseFactory

pytestmark = pytest.mark.django_db


class TestExpenseListView:
    def test_expense_list_view(self, client):
        url = reverse("expenses:list")
        response = client.get(url)
        assert response.status_code == 200

    def test_expense_list_view_with_expenses(self, client):
        ExpenseFactory.create_batch(10)
        url = reverse("expenses:list")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context["object_list"]) == 10
    

class TestExpenseDetailView:
    def test_expense_detail_view(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:detail", kwargs={"pk": expense.pk})
        response = client.get(url)
        assert response.status_code == 200

    def test_expense_detail_view_with_expense(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:detail", kwargs={"pk": expense.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert response.context["object"] == expense


class TestExpenseCreateView:
    def test_expense_create_view(self, client):
        url = reverse("expenses:create")
        response = client.get(url)
        assert response.status_code == 200

    def test_expense_create_view_with_valid_data(self, client):
        url = reverse("expenses:create")
        data = {
            "name": "Test Expense",
            "amount": 100,
            "category": "Food",
           
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert Expense.objects.count() == 1
        assert Expense.objects.first().name == "Test Expense"

    def test_expense_create_view_with_invalid_data(self, client):
        url = reverse("expenses:create")
        data = {
            "title": "Test Expense",
            "amount": 100,
            "category": "Food",
       
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert Expense.objects.count() == 0
        assert ExpenseForm(data).errors == {
            "name": ["This field is required."]
        }


class TestExpenseUpdateView:
    def test_expense_update_view(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:update", kwargs={"pk": expense.pk})
        response = client.get(url)
        assert response.status_code == 200

    def test_expense_update_view_with_valid_data(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:update", kwargs={"pk": expense.pk})
        data = {
            "name": "Test Expense Update View",
            "amount": 100,
            "category": "Food",
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert Expense.objects.count() == 1
        assert Expense.objects.first().name == "Test Expense Update View"

    def test_expense_update_view_with_invalid_data(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:update", kwargs={"pk": expense.pk})
        data = {
            "name": "",
            "amount": 100,
            "category": "Food",
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert Expense.objects.count() == 1
        assert Expense.objects.first().name == expense.name
        assert ExpenseForm(data).errors == {
            "name": ["This field is required."]
        }


class TestExpenseDeleteView:
    def test_expense_delete_view(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:delete", kwargs={"pk": expense.pk})
        response = client.get(url)
        assert response.status_code == 200

    def test_expense_delete_view_with_valid_data(self, client):
        expense = ExpenseFactory()
        url = reverse("expenses:delete", kwargs={"pk": expense.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert Expense.objects.count() == 0

    def test_expense_delete_view_with_invalid_data(self, client):
        url = reverse("expenses:delete", kwargs={"pk": 100})
        response = client.post(url)
        assert response.status_code == 404
        assert Expense.objects.count() == 0