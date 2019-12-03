from django import forms

class ExpanseForm(forms.Form):
    expanse_description = forms.CharField(label='Description', max_length=100)
    expanse_amount = forms.IntegerField(label = 'Amount')
    