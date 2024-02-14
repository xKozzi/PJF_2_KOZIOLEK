

from django.db import models

from django.urls import reverse
from account.models import User
import datetime
from tools.email import send_limit_exceeded_mail


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    limit = models.IntegerField()

    def get_absolute_url(self):
        from finances.views import CategoryListView
        return reverse(CategoryListView.get_view_name())

    def __str__(self):
        return self.name
    
    def get_current_balance(self):
        return self.expense_set.filter(date__month=datetime.date.today().month).aggregate(total_expenses=models.Sum('value'))['total_expenses'] or 0.0


class Expense(models.Model):
    name = models.CharField()
    value = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today())

    def get_absolute_url(self):
        from finances.views import ExpensesListView
        return reverse(ExpensesListView.get_view_name())

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date = datetime.date.today()

        if self.category.get_current_balance() + self.value > self.category.limit:
            send_limit_exceeded_mail(user=self.category.user, category=self.category, expense=self)
        super(Expense, self).save(*args, **kwargs)
