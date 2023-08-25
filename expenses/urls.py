from django.urls import path

from . import views

urlpatterns = [
    path("expenses", views.ExpenseCreateView.as_view(), name="expenses"),
    path("update/<int:pk>", views.ExpenseUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.ExpenseDeleteView.as_view(), name="delete"),
]
