from django import forms

from .models import Expense

class ExpanseForm(forms.Form):
    expanse_description = forms.CharField(label='Description', max_length=100)
    expanse_amount = forms.IntegerField(label = 'Amount')

class ExpanseForm2(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('description', 'amount',)
