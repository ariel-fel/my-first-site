from django import forms

from .models import Expense

class ExpanseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('description', 'amount',)
