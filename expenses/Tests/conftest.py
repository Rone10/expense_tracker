from pytest_factoryboy import register
import pytest

from .factories import ExpenseFactory

register(ExpenseFactory)