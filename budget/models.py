import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class BudgetEntry(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    amount = models.PositiveIntegerField(default=0)
    def __str__(self):
            return self.description


class Expense(models.Model):
    PAYMENT = [
      (1, 'Cash'),
      (2, 'Visa'),
      (3, 'Visa CAL'),
      (4, 'Diners'),]

    entry = models.ForeignKey(BudgetEntry, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    expense_date = models.DateTimeField('date published')
    amount = models.PositiveIntegerField(default=0)
    paymeny_method = models.PositiveSmallIntegerField(choices=PAYMENT, default=1)
    payments = models.PositiveSmallIntegerField(default=1)
    user = models.CharField(max_length=200, default='ariel')

    def __str__(self):
            return self.description
