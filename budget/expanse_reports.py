from django.utils import timezone
from .models import Expense
import datetime
from budget.date_functions import add_month, reduce_month

class ExpanseReport():
    def __init__(self, month, amount, within_budget):
        self.month = month
        self.amount = amount
        self.within_budget = within_budget


def get_expanse_by_month(budget_entry, needed_month):
    start_date = datetime.date(year = needed_month.year, month=needed_month.month, day=1)
    end_date = add_month(start_date)

    expanses = Expense.objects.filter(entry=budget_entry).filter(expense_date__gte=start_date).filter(expense_date__lt=end_date)

    month_sum = 0
    for e in expanses:
        month_sum += e.amount

    return month_sum

def create_month_by_month_report(budget_entry):
    expanse_report = []
    d = timezone.now()

    for i in range(6):
        month_sum = get_expanse_by_month(budget_entry, d)
        
        expanse_report.append(ExpanseReport(d.strftime("%b %y") ,month_sum, month_sum <= budget_entry.amount))

        d = reduce_month(d)

    return expanse_report
