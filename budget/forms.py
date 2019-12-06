from django import forms

from .models import Expense

class ExpanseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('description', 'amount', 'payment_method', 'payments')

class ExpanseFormDate(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('description', 'amount', 'user', 'payment_method', 'payments', 'expense_date')
