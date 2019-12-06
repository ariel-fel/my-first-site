import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class BudgetEntry(models.Model):
    PAYMENT_CYCLE = [
      (1, 'Month'),
      (2, 'Year'),
      (3, 'Week'),]

    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date start')
    end_date = models.DateTimeField('date end')
    amount = models.PositiveIntegerField(default=0)
    budget_cycle = models.PositiveSmallIntegerField(choices=PAYMENT_CYCLE, default=1)
    def __str__(self):
            return self.description

    def is_yearly(self):
      return self.budget_cycle==[item[0] for item in self.PAYMENT_CYCLE if item[1] == 'Year'][0]
    def is_monthly(self):
      return self.budget_cycle==[item[0] for item in self.PAYMENT_CYCLE if item[1] == 'Month'][0]
    def is_weekly(self):
      return self.budget_cycle==[item[0] for item in self.PAYMENT_CYCLE if item[1] == 'Week'][0]
    def get_cycle(self):
      return [item[1] for item in self.PAYMENT_CYCLE if item[0] == self.budget_cycle][0]

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
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT, default=2)
    payments = models.PositiveSmallIntegerField(default=1)
    user = models.CharField(max_length=200, default='ariel')

    def __str__(self):
            return self.description

    def is_cash(self):
      return self.payment_method==[item[0] for item in self.PAYMENT if item[1] == 'Cash'][0]
    def get_payment_method(self):
      return [item[1] for item in self.PAYMENT if item[0] == self.payment_method][0]