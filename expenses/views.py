from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db import models
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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





class ExpenseCreateView(LoginRequiredMixin ,CreateView):
    template_name = 'expenses/create.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses:expenses')
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] =  Expense.objects.all()
     
        categories = Expense.CATEGORIES
        context['categories'] = categories
        total = Expense.objects.all().aggregate(total=models.Sum('amount'))
        context['total'] = total
        cats = {}
        for cat in categories:
            print('cat', cat)
            q = Expense.objects.filter(category=cat[0]).aggregate(total=models.Sum('amount'))['total'] 
            if q:
                cats[cat[0]] = float(q)
            else:
                cats[cat[0]] =  0.00
        context['cats'] = cats
        print(cats)
        return context

    
class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    # model = Expense
    template_name = 'expenses/update.html'
    form_class = ExpenseForm
    queryset = Expense.objects.all()
    success_url = reverse_lazy('expenses:expenses')


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'expenses/delete.html'
    context_object_name = 'expense'
    success_url = reverse_lazy('expenses:expenses')
