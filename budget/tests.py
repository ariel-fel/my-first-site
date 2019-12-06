import datetime

from django.test import TestCase
from django.utils import timezone

from .models import BudgetEntry, Expense

# Create your tests here.
class BudgetEntryModelTests(TestCase):

    def test_positive_budget(self):
        
        negetive_budget = BudgetEntry(amount=500)
        self.assertIs(negetive_budget.amount >= 0, True)
    
    def test_cycle_budget(self):
        
        monthly_budget1 = BudgetEntry(amount=500, budget_cycle=1)
        monthly_budget2 = BudgetEntry(amount=500, budget_cycle=2)
        monthly_budget3 = BudgetEntry(amount=500, budget_cycle=3)
        self.assertIs(monthly_budget1.is_monthly(), True)
        self.assertIs(monthly_budget2.is_monthly(), False)
        self.assertIs(monthly_budget3.is_monthly(), False)
        self.assertIs(monthly_budget1.is_weekly(), False)
        self.assertIs(monthly_budget2.is_weekly(), False)
        self.assertIs(monthly_budget3.is_weekly(), True)
        self.assertIs(monthly_budget1.is_yearly(), False)
        self.assertIs(monthly_budget2.is_yearly(), True)
        self.assertIs(monthly_budget3.is_yearly(), False)

class ExpenseModelTests(TestCase):

    def test_positive_budget(self):
        
        cash_expanse = Expense(amount=500, payment_method = 1)
        self.assertIs(cash_expanse.is_cash(), True)