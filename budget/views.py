from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import BudgetEntry
from .forms import ExpanseForm2

class IndexView(generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'budget_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BudgetEntry.objects.order_by('-amount')

def detail(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)
    #return render(request, 'budget/detail.html', {'budget_entry': budget_entry})
    if request.method == "POST":
        form = ExpanseForm2(request.POST)
    else:
        form = ExpanseForm2()
    # check whether it's valid:
    if form.is_valid():
        expanse = form.save(commit=False)
    
        budget_entry.expense_set.create(
            description = expanse.description,
            expense_date = timezone.now(),
            amount = expanse.amount)

        return HttpResponseRedirect(reverse('budget:expanse', args=(budget_entry.id,)))

    context = {'budget_entry': budget_entry, 'form': form}
    return render(request, 'budget/detail.html', context)

def expanse(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)
    context = {'budget_entry': budget_entry}
    return render(request, 'budget/expanse_done.html', context)

class ExpanseReport():
    def __init__(self, month, amount):
        self.month = month
        self.amount = amount

def status(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)

    expanse_report = []
    expanse_report.append(ExpanseReport(1,3))

    context = {'budget_entry': budget_entry, 'expanse_report':expanse_report }
    return render(request, 'budget/status.html', context)
