from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.db import models
from django.core.paginator import Paginator
from .forms import ExpenseForm
from .models import Expense
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    template_name = "expenses/create.html"
    form_class = ExpenseForm
    success_url = reverse_lazy("expenses:expenses")

    def get_context_data(self, **kwargs):
        self.object = None
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expense.objects.all()
        expenses = Expense.objects.all()
        paginator = Paginator(expenses, 15)  # Show 5 expenses per page.

        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["expenses"] = page_obj

        categories = Expense.CATEGORIES
        context["categories"] = categories
        total = Expense.objects.all().aggregate(total=models.Sum("amount"))
        context["total"] = total
        cats = {}
        for cat in categories:
            print("cat", cat)
            q = Expense.objects.filter(category=cat[0]).aggregate(
                total=models.Sum("amount")
            )["total"]
            if q:
                cats[cat[0]] = float(q)
            else:
                cats[cat[0]] = 0.00
        context["cats"] = cats
        print(cats)
        return context

    def get(self, request, *args, **kwargs):
        print("inside get")
        context = self.get_context_data(**kwargs)
        print("context", context)
        q = request.GET.get("search")

        search_page = request.GET.get("search_page")
        context["prev_q"] = request.GET.get("prev_q")
        print("q", q)
        results = None

        if q:
            context["search"] = True
            context["prev_q"] = q
            results = Expense.objects.filter(
                name__icontains=self.request.GET.get("search")
            )
            if results:
                page = self.request.GET.get("search_page", 1)
                paginator = Paginator(results, 1)
                page_obj = paginator.page(page)
                context["search_results"] = page_obj
                context["expenses"] = []
                # context["expenses"] = results
        elif search_page:
            prev_q = request.GET.get("prev_q")
            results = Expense.objects.filter(name__icontains=prev_q)

            paginator = Paginator(results, 1)
            page_obj = paginator.page(search_page)
            context["search_results"] = page_obj
            context["expenses"] = []
        if q and not results:
            context["expenses"] = []

        return self.render_to_response(context)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    # model = Expense
    template_name = "expenses/update.html"
    form_class = ExpenseForm
    queryset = Expense.objects.all()
    success_url = reverse_lazy("expenses:expenses")


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = "expenses/delete.html"
    context_object_name = "expense"
    success_url = reverse_lazy("expenses:expenses")
