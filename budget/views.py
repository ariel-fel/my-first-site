from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import BudgetEntry
from .forms import ExpanseForm

class IndexView(generic.ListView):
    template_name = 'budget/index.html'
    context_object_name = 'budget_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return BudgetEntry.objects.order_by('-amount')

def detail(request, pk):
    budget_entry = get_object_or_404(BudgetEntry,pk=pk)
    #return render(request, 'budget/detail.html', {'budget_entry': budget_entry})
    form = ExpanseForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        return HttpResponse('/thanks/')

    context = {'budget_entry': budget_entry, 'form': form}
    return render(request, 'budget/detail.html', context)

def expanse(request, entry_id):
    budget_entry = get_object_or_404(BudgetEntry,pk=entry_id)
    context = {'budget_entry': budget_entry}
    return render(request, 'budget/expanse_done.html', context)
    
def make_expanse(request, entry_id):
    budget_entry = get_object_or_404(BudgetEntry,pk=entry_id)
    expanse_amount = request.POST['expanse_amount']
    expanse_description = request.POST['expanse_description']
    
    budget_entry.expense_set.create(
        description = expanse_description,
        expense_date = timezone.now(),
        amount = expanse_amount)

    return HttpResponseRedirect(reverse('budget:expanse', args=(budget_entry.id,)))
