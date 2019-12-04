import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class BudgetEntry(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount = models.IntegerField(default=0)
    amount_spent = models.IntegerField(default=0)
    def __str__(self):
            return self.description
    def has_any_left(self):
        return self.amount_spent < self.amount

class Expense(models.Model):
    entry = models.ForeignKey(BudgetEntry, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    expense_date = models.DateTimeField('date published')
    amount = models.IntegerField(default=0)
    def __str__(self):
            return self.description
    def is_violating_budget(self):
        return self.amount > 0

