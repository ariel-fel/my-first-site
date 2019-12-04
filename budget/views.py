from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import BudgetEntry, Expense
from .forms import ExpanseForm
import datetime
from budget.date_functions import add_month, reduce_month
from budget.expanse_reports import get_expanse_by_month, create_month_by_month_report

class IndexView(generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'budget_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BudgetEntry.objects.order_by('-amount')


def detail(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)

    monthly_expanses = get_expanse_by_month(budget_entry, timezone.now())
    if request.method == "POST":
        form = ExpanseForm(request.POST)
    else:
        form = ExpanseForm()
    # check whether it's valid:
    if form.is_valid():
        expanse = form.save(commit=False)
    
        budget_entry.expense_set.create(
            description = expanse.description,
            expense_date = timezone.now(),
            amount = expanse.amount)

        return HttpResponseRedirect(reverse('budget:expanse', args=(budget_entry.id,)))

    context = {'budget_entry': budget_entry, 'form': form, 'monthly_expanses':monthly_expanses}
    return render(request, 'budget/detail.html', context)

def expanse(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)
    context = {'budget_entry': budget_entry}
    return render(request, 'budget/expanses.html', context)

def status(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)

    expanse_report = create_month_by_month_report(budget_entry)

    context = {'budget_entry': budget_entry, 'expanse_report':expanse_report }
    return render(request, 'budget/status.html', context)
