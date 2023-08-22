from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('list', views.ExpenseListView.as_view(), name='list'),
    path('expenses', views.ExpenseCreateView.as_view(), name='expenses'),
    path('update/<int:pk>', views.ExpenseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ExpenseDeleteView.as_view(), name='delete'),
]