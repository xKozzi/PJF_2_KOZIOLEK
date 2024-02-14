from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views.generic import UpdateView, ListView, CreateView, TemplateView, DeleteView
from finances.models import Expense, Category
from django.db.models import Sum
from tools.views import AbstractView
from finances.forms import ExpenseForm, CategoryForm
import datetime


class FinancesGenericView(AbstractView):
    app_name = "finances"


class ExpensesListView(FinancesGenericView, ListView):
    view_name = "expense_list"
    template_name = "expense_list.html"
    model = Expense
    queryset = Expense.objects.all()
    context_object_name = "expenses"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["month_title"] = datetime.datetime.now().strftime('%B')
        data["limit_sum"] = Category.objects.filter(user=self.request.user).aggregate(limit_sum=Sum('limit'))['limit_sum'] or 0
        data["expenses_sum"] = Expense.objects.filter(category__user=self.request.user, date__month=datetime.date.today().month).aggregate(expense_sum=Sum('value'))['expense_sum'] or 0
        return data


class CategoryListView(FinancesGenericView, ListView):
    view_name = "category_list"
    template_name = "category_list.html"
    model = Category
    context_object_name = "categories"

    def get_queryset(self) -> QuerySet[Any]:
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["month_title"] = datetime.datetime.now().strftime('%B')
        data["limit_sum"] = Category.objects.filter(user=self.request.user).aggregate(limit_sum=Sum('limit'))['limit_sum'] or 0
        data["expenses_sum"] = Expense.objects.filter(category__user=self.request.user, date__month=datetime.date.today().month).aggregate(expense_sum=Sum('value'))['expense_sum'] or 0
        return data


class ExpensesCreateView(FinancesGenericView, CreateView):
    template_name = "expense_create.html"
    view_name = "expense_create"
    model = Expense
    form_class = ExpenseForm


class CategoryCreateView(FinancesGenericView, CreateView):
    template_name = "category_create.html"
    view_name = "category_create"
    model = Category
    form_class = CategoryForm

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryUpdateView(FinancesGenericView, UpdateView):
    template_name = "category_create.html"
    view_name = "category_update"
    model = Category
    form_class = CategoryForm

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ExpenseUpdateView(FinancesGenericView, UpdateView):
    template_name = "expense_create.html"
    view_name = "expense_update"
    model = Expense
    form_class = ExpenseForm
    

class CategoryDeleteView(FinancesGenericView, DeleteView):
    view_name = "category_delete"
    model = Category

    def get_success_url(self) -> str:
        from finances.views import CategoryListView
        return reverse(CategoryListView.get_view_name())


class ExpenseDeleteView(FinancesGenericView, DeleteView):
    view_name = "expense_delete"
    model = Expense

    def get_success_url(self) -> str:
        from finances.views import ExpensesListView
        return reverse(ExpensesListView.get_view_name())


class ExpenseCalculatorView(FinancesGenericView, TemplateView):
    template_name = "expense_calculator.html"
    view_name = "expense_calculator"


class ExpensesForCategoryListView(FinancesGenericView, ListView):
    template_name = "expense_list.html"
    view_name = "expenses_for_category"
    model = Expense
    context_object_name = "expenses"

    def get_queryset(self) -> QuerySet[Any]:
        pk = self.kwargs.get("pk")
        if pk:
            self.category = Category.objects.get(pk=pk)
        return Expense.objects.filter(category=self.category, date__month=datetime.date.today().month)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["month_title"] = datetime.datetime.now().strftime('%B') + f" for {self.category} category"
        data["limit_sum"] = self.category.limit
        data["expenses_sum"] = Expense.objects.filter(category=self.category, date__month=datetime.date.today().month).aggregate(expense_sum=Sum('value'))['expense_sum'] or 0
        return data