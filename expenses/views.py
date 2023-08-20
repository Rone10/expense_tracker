from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


def index(request):
    return render(request, 'expenses/index.html')


# class ExpenseListView(ListView):
#     model = Expense
#     template_name = 'expenses/list.html'
#     context_object_name = 'expenses'

#     def get_conteext_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['expenses'] = context['expenses'].filter(user=self.request.user)
#         # context['count'] = context['expenses'].filter(user=self.request.user).count()
#         context['form'] = ExpenseForm()
#         return context


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expenses/detail.html'
    context_object_name = 'expense'


class ExpenseCreateView(CreateView):
    template_name = 'expenses/create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses:expenses')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] =  Expense.objects.all()
        return context

    # def get_success_url(self) -> str:
    #     return super().get_success_url()


class ExpenseUpdateView(UpdateView):
    # model = Expense
    template_name = 'expenses/update.html'
    form_class = ExpenseForm
    queryset = Expense.objects.all()


    def get_success_url(self) -> str:
        return super().get_success_url()


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expenses/delete.html'
    context_object_name = 'expense'
    success_url = reverse_lazy('expenses:expenses')
