from django.urls import re_path
from finances.views import (
    ExpensesListView,
    ExpensesCreateView,
    CategoryListView,
    CategoryCreateView,
    ExpenseCalculatorView,
    CategoryDeleteView,
    ExpenseDeleteView,
    ExpenseUpdateView,
    CategoryUpdateView,
    ExpensesForCategoryListView
)

urlpatterns = [
    re_path(r"expenses_list$", view=ExpensesListView.as_view(), name=ExpensesListView.view_name),
    re_path(r"category_list$", view=CategoryListView.as_view(), name=CategoryListView.view_name),
    re_path(r"^category_delete/(?P<pk>\d+)$", view=CategoryDeleteView.as_view(), name=CategoryDeleteView.view_name),
    re_path(r"^expense_delete/(?P<pk>\d+)$", view=ExpenseDeleteView.as_view(), name=ExpenseDeleteView.view_name),
    re_path(r"^expense/edit/(?P<pk>\d+)$", view=ExpenseUpdateView.as_view(), name=ExpenseUpdateView.view_name),
    re_path(r"^category/edit/(?P<pk>\d+)$", view=CategoryUpdateView.as_view(), name=CategoryUpdateView.view_name),
    re_path(r"new_expense$", view=ExpensesCreateView.as_view(), name=ExpensesCreateView.view_name),
    re_path(r"new_category$", view=CategoryCreateView.as_view(), name=CategoryCreateView.view_name),
    re_path(r"expense_calculator$", view=ExpenseCalculatorView.as_view(), name=ExpenseCalculatorView.view_name),
    re_path(r"expenses/(?P<pk>\d+)$", view=ExpensesForCategoryListView.as_view(), name=ExpensesForCategoryListView.view_name),
]