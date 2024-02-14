from django import forms
from finances.models import Expense, Category


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("value", "name", "category")


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("user", "name", "limit")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['user'].widget = forms.HiddenInput()