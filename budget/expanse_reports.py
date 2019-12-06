from django.utils import timezone
from .models import Expense
import datetime
from budget.date_functions import add_month, reduce_month

class ExpanseReport():
    def __init__(self, month, amount, within_budget):
        self.month = month
        self.amount = amount
        self.within_budget = within_budget

def cycle_start(budget_entry, my_date):
    if budget_entry.is_yearly():
        start_date = datetime.date(year = my_date.year, month=1, day=1)
    elif budget_entry.is_weekly():
        start_date = my_date
        if my_date.weekday()!=6: # if not Sunday (Sunday is 6 not as Jewish calender)
            start_date = my_date  - my_date.weekday() - 1
    else :
        start_date = datetime.date(year = my_date.year, month=my_date.month, day=1)
    
    return start_date

def add_cycle(budget_entry, my_date):
    if budget_entry.is_yearly():
        end_date = datetime.date(year = my_date.year + 1, month=my_date.month, day=my_date.day)
    elif budget_entry.is_weekly():
        end_date = my_date +  datetime.timedelta(days=7)
    else :
        end_date = add_month(my_date)
    
    return end_date

def reduce_cycle(budget_entry, my_date):
    if budget_entry.is_yearly():
        end_date = datetime.date(year = my_date.year - 1, month=my_date.month, day=my_date.day)
    elif budget_entry.is_weekly():
        end_date = my_date -  datetime.timedelta(days=7)
    else :
        end_date = reduce_month(my_date)
    
    return end_date

def get_expanse_by_cycle(budget_entry, needed_month):
    
    start_date = cycle_start(budget_entry, needed_month)
    end_date = add_cycle(budget_entry, start_date)

    expanses = Expense.objects.filter(entry=budget_entry).filter(expense_date__gte=start_date).filter(expense_date__lt=end_date)

    month_sum = 0
    for e in expanses:
        month_sum += e.amount

    return month_sum

def create_cycle_by_cycle_report(budget_entry):
    expanse_report = []
    d = timezone.now()

    for i in range(6):
        month_sum = get_expanse_by_cycle(budget_entry, d)
        
        expanse_report.append(ExpanseReport(d.strftime("%b %y") ,month_sum, month_sum <= budget_entry.amount))

        d = reduce_cycle(budget_entry, d)

    return expanse_report
