from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.ExpenseListView.as_view(), name='list'),
    path('detail/<int:pk>', views.ExpenseDetailView.as_view(), name='detail'),
    path('create', views.ExpenseCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.ExpenseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.ExpenseDeleteView.as_view(), name='delete'),
]