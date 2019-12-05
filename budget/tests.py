import datetime

from django.test import TestCase
from django.utils import timezone

from .models import BudgetEntry, Expense

# Create your tests here.
class BudgetEntryModelTests(TestCase):

    def test_positive_budget(self):
        
        negetive_budget = BudgetEntry(amount=-500)
        print(negetive_budget.amount)
        self.assertIs(negetive_budget.amount >= 0, True)