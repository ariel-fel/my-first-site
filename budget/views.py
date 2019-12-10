from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import BudgetEntry, Expense
from .forms import ExpanseForm, ExpanseFormDate
import datetime
from budget.expanse_reports import get_expanse_by_cycle, create_cycle_by_cycle_report

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'budget_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BudgetEntry.objects.order_by('-amount')


@login_required
def remove_expanse(request, pk):
    expense_entry = get_object_or_404(Expense,pk=pk)
    expense_entry.delete()

    return HttpResponseRedirect(reverse('budget:index', args=()))
    

@login_required
def edit_expanse(request, pk):
    expense_entry = get_object_or_404(Expense,pk=pk)
    prefill = {'description':expense_entry.description, 'amount':expense_entry.amount, 'expense_date': expense_entry.expense_date, 'user' : expense_entry.user, 'payment_method':expense_entry.payment_method, 'payments': expense_entry.payments}
    if request.method == "POST":
        form = ExpanseFormDate(request.POST,initial = prefill)
    else:
        form = ExpanseFormDate(initial = prefill)
    # check whether it's valid:
    if form.is_valid():
        expanse = form.save(commit=False)

        expense_entry.description = expanse.description
        expense_entry.amount = expanse.amount
        expense_entry.expense_date = expanse.expense_date
        expense_entry.user = expanse.user
        expense_entry.payment_method = expanse.payment_method
        expense_entry.payments = expanse.payments
        expense_entry.save()

        return HttpResponseRedirect(reverse('budget:index', args=()))

    context = {'expense_entry': expense_entry, 'form': form }
    return render(request, 'budget/edit_expanse.html', context)

@login_required
def detail(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)

    sum_expanses = get_expanse_by_cycle(budget_entry, timezone.now())
    budget_cycle = budget_entry.get_cycle()

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
            user = request.user.username,
            payment_method = expanse.payment_method,
            payments = expanse.payments,
            amount = expanse.amount)

        return HttpResponseRedirect(reverse('budget:expanse', args=(budget_entry.id,)))

    context = {'budget_entry': budget_entry, 'form': form, 'sum_expanses':sum_expanses, 'budget_cycle':budget_cycle}
    return render(request, 'budget/detail.html', context)

@login_required
def expanse(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)
    context = {'budget_entry': budget_entry}
    return render(request, 'budget/expanses.html', context)

@login_required
def status(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)

    expanse_report = create_cycle_by_cycle_report(budget_entry)

    context = {'budget_entry': budget_entry, 'expanse_report':expanse_report }
    return render(request, 'budget/status.html', context)
